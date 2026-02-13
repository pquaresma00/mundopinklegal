<?php
session_start();
header('Content-Type: application/json');

$rawBody = file_get_contents('php://input');
$input = json_decode($rawBody, true);
if (!is_array($input)) {
    $input = [];
}

// pega o ID da transação vindo do JS ou por fallback
$transactionId =
    ($_GET['order_id'] ?? null) ??
    ($_GET['transactionId'] ?? null) ??
    ($input['order_id'] ?? null) ??
    ($input['transactionId'] ?? null) ??
    ($input['id'] ?? null) ??
    ($_POST['transaction_id'] ?? null) ??
    ($_POST['order_id'] ?? null);

if (!$transactionId) {
    echo json_encode([
        'status'  => 'waiting_payment',
        'message' => 'ID da transação não encontrado.'
    ]);
    exit;
}

// mesma URL encriptada da Dutty Pay usada no pagamento
$apiUrl = 'https://www.pagamentos-seguros.app/api-pix/kVAU1qD7_pqKdODGU97NT84eirgu57zLxXBD-hxBFHz2Si2DXcEeiFMj24rte05IWMXocGiGDHYlr9IqZF_hLQ';

// monta URL de consulta com o transactionId
$consultUrl = $apiUrl . '?transactionId=' . urlencode($transactionId);

$ch = curl_init($consultUrl);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER     => [
        'Content-Type: application/json'
    ],
]);

$response  = curl_exec($ch);
$httpCode  = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

if ($response === false) {
    echo json_encode([
        'status'  => 'error',
        'message' => 'Erro ao executar requisição CURL: ' . $curlError
    ]);
    exit;
}

if ($httpCode < 200 || $httpCode >= 300) {
    echo json_encode([
        'status'   => 'error',
        'message'  => 'Erro ao verificar status do pagamento.',
        'httpCode' => $httpCode,
        'raw'      => $response
    ]);
    exit;
}

$decoded = json_decode($response, true);
if ($decoded === null) {
    echo json_encode([
        'status'  => 'error',
        'message' => 'Resposta inválida da API',
        'raw'     => $response
    ]);
    exit;
}

// tenta mapear o campo de status da API
$rawStatus =
    $decoded['status'] ??
    ($decoded['data']['status'] ?? null) ??
    ($decoded['payment']['status'] ?? null) ??
    'PENDING';

// Mapeia o status da API para o formato que o JS espera
// A API retorna: PENDING, PAID, COMPLETED, etc.
// O JS espera: mapped_status === "paid"
$mappedStatus = 'waiting_payment';
if (is_string($rawStatus)) {
    $rawStatusUpper = strtoupper(trim($rawStatus));
    if ($rawStatusUpper === 'PAID' || $rawStatusUpper === 'APPROVED' || $rawStatusUpper === 'CONFIRMED' || $rawStatusUpper === 'COMPLETED') {
        $mappedStatus = 'paid';
    } elseif ($rawStatusUpper === 'PENDING' || $rawStatusUpper === 'WAITING') {
        $mappedStatus = 'waiting_payment';
    } elseif ($rawStatusUpper === 'FAILED' || $rawStatusUpper === 'REJECTED' || $rawStatusUpper === 'CANCELLED') {
        $mappedStatus = 'failed';
    }
}

// resposta no formato que o JS espera
// O JS verifica y.status === "COMPLETED", então retornamos o status original da API
echo json_encode([
    'status' => $rawStatus, // status original da API (PENDING ou COMPLETED)
    'mapped_status' => $mappedStatus, // status mapeado para o JS (waiting_payment ou paid)
    'response' => $decoded // pode remover depois, é só pra debug
], JSON_UNESCAPED_UNICODE);
