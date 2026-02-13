<?php
// /api/get_public_config.php

header('Content-Type: application/json; charset=utf-8');

$config = [
  "success" => true,

  // Seu front usa isso em alguns pontos:
  "exigirCpf" => false,

  // Taxa de proteção (se você usa no checkout quando total é 0)
  "taxaProtecao" => [
    "ativo" => true,
    "valor" => 1685, // centavos (R$ 16,85)
    "nome"  => "Taxa de Proteção de Entrega"
  ],

  // FRETES (valores em centavos)
  "fretes" => [
    [
      "id" => "sedex",
      "name" => "Correios PAC",
      "description" => "8-12 dias úteis",
      "price" => 1936,          // <-- GRÁTIS
      "ativo" => true,
      "isDefault" => true
    ],
    [
      "id" => "pac",
      "name" => "Jadlog",
      "description" => "6-8 dias úteis",
      "price" => 2271,
      "ativo" => true,
      "isDefault" => false
    ],
    [
      "id" => "jadlog",
      "name" => "Sedex Full",
      "description" => "Chegará amanhã",
      "price" => 2688,
      "ativo" => true,
      "isDefault" => false
    ]
  ]
];

echo json_encode($config, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
exit;