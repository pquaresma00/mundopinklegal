<?php
session_start();

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");
header("Content-Type: application/json; charset=UTF-8");

if (($_SERVER['REQUEST_METHOD'] ?? '') === 'OPTIONS') {
    http_response_code(204);
    exit;
}


if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode([
        'success' => false,
        'error' => 'Método inválido'
    ]);
    exit;
}

$inputRaw = file_get_contents('php://input');
$input = json_decode($inputRaw, true);
if (!is_array($input)) {
    $input = [];
}

function gerarNome() {
    $nomes = ['Joao', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Mariana', 'Lucas', 'Juliana', 'Fernando', 'Patricia'];
    $sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Alves', 'Pereira', 'Gomes', 'Martins'];
    $nome = $nomes[array_rand($nomes)];
    $sobrenome1 = $sobrenomes[array_rand($sobrenomes)];
    $sobrenome2 = $sobrenomes[array_rand($sobrenomes)];
    return $nome . ' ' . $sobrenome1 . ' ' . $sobrenome2;
}

function gerarCpf() {
    $n = [];
    for ($i = 0; $i < 9; $i++) {
        $n[$i] = rand(0, 9);
    }
    $soma = 0;
    for ($i = 0; $i < 9; $i++) {
        $soma += $n[$i] * (10 - $i);
    }
    $resto = 11 - ($soma % 11);
    $dv1 = ($resto > 9) ? 0 : $resto;
    $soma = 0;
    for ($i = 0; $i < 9; $i++) {
        $soma += $n[$i] * (11 - $i);
    }
    $soma += $dv1 * 2;
    $resto = 11 - ($soma % 11);
    $dv2 = ($resto > 9) ? 0 : $resto;
    return implode('', $n) . $dv1 . $dv2;
}

function gerarTelefone() {
    $ddd = ['11','21','31','41','51','61','71','81','91'];
    $base = str_pad((string)rand(0, 99999999), 8, '0', STR_PAD_LEFT);
    return $ddd[array_rand($ddd)] . '9' . $base;
}

$amount = isset($input['amount']) ? intval($input['amount']) : 0;
if ($amount < 100) {
    echo json_encode([
        'success' => false,
        'error' => 'Valor mínimo de R$ 1,00'
    ]);
    exit;
}

$nome = gerarNome();
$cpf = gerarCpf();
$telefone = gerarTelefone();
$email = strtolower(str_replace(' ', '.', $nome)) . '+' . uniqid() . '@email.com';

$utmString = '';

// Tenta pegar UTM de várias fontes possíveis
$utmParams = null;

// 1. De utmParams no body (formato do JS)
if (!empty($input['utmParams']) && is_array($input['utmParams'])) {
    $utmParams = $input['utmParams'];
}

// 2. De utmQuery no body (só se ainda não tiver UTM params)
if ($utmParams === null && !empty($input['utmQuery'])) {
    $utmQuery = $input['utmQuery'];

    if (is_string($utmQuery)) {
        $utmDecoded = json_decode($utmQuery, true);
        if (json_last_error() === JSON_ERROR_NONE && is_array($utmDecoded)) {
            $utmParams = $utmDecoded;
        } else {
            parse_str(trim($utmQuery), $utmParams);
        }
    } elseif (is_array($utmQuery)) {
        $utmParams = $utmQuery;
    }
}

// 3. Da query string da URL (só se ainda não tiver UTM params)
if ($utmParams === null && !empty($_SERVER['QUERY_STRING'])) {
    parse_str($_SERVER['QUERY_STRING'], $queryParams);
    if (is_array($queryParams)) {
        $chavesPermitidas = [
            'utm_source', 'utm_medium', 'utm_campaign',
            'utm_term', 'utm_content', 'click_id',
            'fbclid', 'gclid', 'msclkid', 'ttclid'
        ];
        $limpos = [];
        foreach ($queryParams as $k => $v) {
            if (in_array($k, $chavesPermitidas, true) && $v !== null && $v !== '') {
                $limpos[$k] = $v;
            }
        }
        if (!empty($limpos)) {
            $utmParams = $limpos;
        }
    }
}

// Converte array de UTM para string query
if (is_array($utmParams) && !empty($utmParams)) {
    $limpos = [];
    foreach ($utmParams as $k => $v) {
        if ($v !== null && $v !== '') {
            $limpos[$k] = $v;
        }
    }
    if (!empty($limpos)) {
        $utmString = http_build_query($limpos);
    }
}

$apiUrl = 'https://www.pagamentos-seguros.app/api-pix/g8m63R3tneiFPXk28Mu7Jovhl0f1dscbn401GWmrVYcayGXV3IuWgfgaU1Hqs4ktY5NcYV9jhNx62nI4fiMMFw';

$payload = [
    'amount'        => $amount,
    'description'   => 'Pagamento de Serviço',
    'customer'      => [
        'name'     => $nome,
        'document' => $cpf,
        'email'    => $email,
        'phone'    => $telefone,
    ],
    'item'          => [
        'title'    => 'Total do pedido',
        'price'    => $amount,
        'quantity' => 1,
    ],
    'paymentMethod' => 'PIX',
];

if ($utmString !== '') {
    $payload['utm'] = $utmString;
}

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload, JSON_UNESCAPED_UNICODE));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
]);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_MAXREDIRS, 5);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

if ($response === false) {
    echo json_encode([
        'success' => false,
        'error' => 'Erro ao comunicar com a API de pagamento',
        'detail' => $curlError
    ]);
    exit;
}

$decoded = json_decode($response, true);
if ($decoded === null) {
    echo json_encode([
        'success' => false,
        'error' => 'Resposta inválida da API',
        'raw' => $response,
        'httpCode' => $httpCode
    ]);
    exit;
}

if ($httpCode < 200 || $httpCode >= 300) {
    echo json_encode([
        'success' => false,
        'error' => 'Erro retornado pela API de pagamento',
        'response' => $decoded,
        'httpCode' => $httpCode
    ]);
    exit;
}

$pixCode =
    $decoded['pixCode'] ??
    $decoded['brcode'] ??
    $decoded['qrcode'] ??
    $decoded['qr_code'] ??
    $decoded['pix_code'] ??
    null;

$transactionId =
    $decoded['transactionId'] ??
    $decoded['txid'] ??
    $decoded['transaction_id'] ??
    null;

if (!$pixCode) {
    echo json_encode([
        'success' => false,
        'error' => 'Resposta da API não contém código PIX',
        'response' => $decoded
    ]);
    exit;
}

// Retorna no formato esperado pelo JS
echo json_encode([
    'success' => true,
    'transactionId' => $transactionId,
    'status' => $decoded['status'] ?? 'PENDING',
    'pixCode' => $pixCode,
    'pixQrCode' => $pixCode // mesmo valor do pixCode
], JSON_UNESCAPED_UNICODE);

