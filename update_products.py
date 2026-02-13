import re

with open('assets/index-WKGCUSBO.js', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# PRODUCT so (id:100) - KIT 5 BODY SPLASH (slug: kit-melancia)
# ============================================================

# Replace description
old_desc_mel = """O Kit Cuide-se Bem Melancia é a escolha perfeita para quem busca uma rotina de autocuidado completa, com produtos que oferecem frescor, hidratação e uma fragrância deliciosa de melancia. Este kit reúne sete itens essenciais para cuidados diários, proporcionando uma experiência sensorial única.

1. Sabonete Líquido Corporal Cuide-se Bem Melancia 150ml
Limpa suavemente a pele, deixando-a perfumada e com sensação de frescor. Sua fórmula contém extrato de melancia, proporcionando uma espuma cremosa e agradável.

2. Gel Esfoliante Corporal Cuide-se Bem Melancia 150g
Promove uma esfoliação delicada, removendo células mortas e deixando a pele macia e renovada. Ideal para uso semanal.

3. Gel Hidratante Desodorante Corporal Cuide-se Bem Melancia 200g
Hidrata profundamente a pele, com rápida absorção e toque refrescante. Sua fragrância de melancia proporciona uma sensação revigorante.

4. Desodorante Roll-On Cuide-se Bem Melancia 55ml
Oferece proteção eficaz contra odores, mantendo as axilas frescas e perfumadas ao longo do dia.

5. Máscara Facial Noturna Cuide-se Bem Melancia 50g
Enquanto você dorme, esta máscara atua na renovação da pele, deixando-a hidratada, radiante e com aparência saudável pela manhã.

6. Balm Labial Intense Cuide-se Bem Melancia 6,2g
Hidrata e protege os lábios, proporcionando um toque de cor natural e brilho suave. Pode ser usado também como blush para um efeito corado.

7. Nécessaire Exclusiva Cuide-se Bem Melancia
Uma nécessaire prática e estilosa para armazenar e transportar seus produtos com segurança e charme.

Este kit é vegano e cruelty-free, alinhado com o compromisso de Wepink com a sustentabilidade e o bem-estar animal."""

new_desc_mel = """O Kit 5 Body Splash Wepink é a escolha perfeita para quem ama variedade e fragrâncias marcantes. Este kit exclusivo reúne cinco body splashes das linhas mais desejadas da Wepink, proporcionando opções para todos os momentos e estilos.

1. Body Splash Liberté Deo Colônia 200ml
Fragrância floral fresca e sofisticada, com notas de flores brancas e um toque cítrico. Ideal para o dia a dia, transmite leveza e feminilidade.

2. Body Splash Deo Colônia 200ml
A fragrância clássica da Wepink em formato body splash. Notas florais e frutais se combinam para uma perfumação suave e envolvente, perfeita para qualquer ocasião.

3. Obsessed Deo Colônia 200ml
Uma fragrância intensa e marcante, com notas de amora, cereja e maçã. Para mulheres que gostam de ousar e deixar sua marca por onde passam.

4. RED Deo Colônia 200ml
Fragrância vibrante e apaixonante, com notas de frutas vermelhas, avelã, cacau e castanha da Índia. Sensual e envolvente, perfeita para momentos especiais.

5. Infinity Body Splash Deo Colônia 200ml
Fragrância sofisticada e duradoura, com notas florais e amadeiradas. Elegante e versátil, ideal para quem busca uma perfumação que acompanha do dia à noite.

Todos os body splashes Wepink possuem fórmula vegana e cruelty-free, com perfumação refrescante e de longa duração. Um kit completo para quem ama se perfumar e ter opções para cada momento."""

content = content.replace(old_desc_mel, new_desc_mel)

# Replace features for kit-melancia
content = content.replace('"01 Sabonete Líquido Corporal 150ml","01 Gel Esfoliante Corporal 150g","01 Gel Hidratante Desodorante Corporal 200g","01 Desodorante Roll-On 55ml","01 Máscara Facial Noturna 50g","01 Balm Labial Intense 6,2g","01 Nécessaire Exclusiva"',
                          '"01 Body Splash Liberté Deo Colônia 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash Deo Colônia 200ml"')

# Replace reviews for kit-melancia
content = content.replace('A linha Melancia é refrescante demais! Perfeita para o verão, o cheiro é delicioso e não enjoa.',
                          'As 5 fragrâncias são incríveis! Cada body splash tem sua personalidade. Meu favorito é o Obsessed!')
content = content.replace('CHEIRO MARAVILHOSO',
                          'KIT MARAVILHOSO', 1)  # only first occurrence
content = content.replace('Amei ter 7 produtos! A máscara noturna é incrível e o lip tint é muito prático.',
                          'Ter 5 opções de fragrância é demais! Uso uma diferente a cada dia. Todas fixam super bem.')
content = content.replace('KIT COMPLETO',
                          'FRAGRÂNCIAS PERFEITAS', 1)
content = content.replace('Perfeito para dias quentes! A colônia Egeo Melancia é viciante, uso todos os dias.',
                          'O RED é meu favorito! Fragrância intensa e sensual. Mas o Liberté também é divino!')
content = content.replace('SUPER FRESQUINHO',
                          'AMEI CADA UM')
content = content.replace('O gel corporal é super refrescante e a loção hidrata muito bem. Vale cada centavo!',
                          'O Infinity é sofisticado e o Obsessed é marcante. Kit perfeito para quem ama se perfumar!')
content = content.replace('Ganhei de presente e fiquei apaixonada! Os produtos são de altíssima qualidade.',
                          'Ganhei de presente e amei! 5 body splashes lindos da Wepink por um preço incrível.')

# Also update shortDescription for kit-melancia
content = content.replace('uma essência mágica e elegante, que revela a ousadia de uma pele bem perfumada.',
                          '5 fragrâncias exclusivas Wepink para todos os momentos do seu dia.')

# ============================================================
# PRODUCT 0 - Kit Bloquinho da Vivibora VF e 5 Body Splash (slug: kit-body-splash-dream)
# ============================================================

old_desc_0 = """O Kit Body Splash Dream Wepink reúne  Uma coleção completa que vai das fragrâncias mais suaves às mais intensas, ideal para diferentes momentos e estilos.

ITENS INCLUSOS NO KIT

Dream Amor No Ar Body Splash 200ml \u2013 Floral Amadeirada leve e romântica, com notas de Âmbar, Sândalo, Baunilha, Bergamota, Cassis, Rosa e Flor de Lótus.

Dream Viagem Encantada Body Splash 200ml \u2013 Floral Gourmand divertido, com a cremosidade do Suspiro e o brilho adocicado da Pera Caramelizada.

Dream Espelho Secreto Body Splash 200ml \u2013 Fragrância envolvente e marcante, que traduz mistério, feminilidade e personalidade.

Dream Jardim dos Mistérios Body Splash 200ml \u2013 Fragrância fresca e intrigante, com combinação equilibrada entre notas florais e verdes.

Dream Filtro dos Sonhos Body Splash 200ml \u2013 Perfume leve e aconchegante, ideal para momentos de tranquilidade e bem-estar.

Dream Céu de Baunilha Body Splash 200ml \u2013 Oriental Gourmand adocicado, com notas de Baunilha, Damasco, Frutas Secas, Pimenta Rosa e Flor Solar.

Dream Banho de Sorte Body Splash 200ml \u2013 Fragrância vibrante e positiva, perfeita para começar o dia com energia e frescor.

Dream Doce Tarde Body Splash 200ml \u2013 Doce na medida certa, com perfumação suave e confortável para o uso diário.

MAIS SOBRE O KIT

Todos os Body Splashes da linha Dream possuem fórmula vegana, não são testados em animais e oferecem perfumação refrescante, ideal para reaplicação ao longo do dia. Um kit completo para quem ama variedade, autocuidado e fragrâncias que acompanham todos os momentos."""

new_desc_0 = """O Kit Bloquinho da Vivibora VF Wepink é uma edição especial que combina o icônico perfume Bloquinho da Vivibora VF com 5 body splashes exclusivos da Wepink. Uma coleção completa para quem ama fragrâncias marcantes e variedade no dia a dia.

ITENS INCLUSOS NO KIT

Bloquinho da Vivibora VF Deo Colônia 100ml \u2013 Fragrância feminina vibrante e envolvente, com notas florais e frutais que traduzem a energia e a personalidade da mulher Wepink.

Body Splash Liberté Deo Colônia 200ml \u2013 Floral fresca e sofisticada, com notas de flores brancas e um toque cítrico. Leveza e feminilidade para o dia a dia.

Body Splash Deo Colônia 200ml \u2013 A fragrância clássica da Wepink em formato body splash. Notas florais e frutais suaves e envolventes.

Obsessed Deo Colônia 200ml \u2013 Fragrância intensa e marcante, com notas de amora, cereja e maçã. Para quem gosta de ousar.

RED Deo Colônia 200ml \u2013 Vibrante e apaixonante, com notas de frutas vermelhas, avelã e cacau. Sensual e envolvente.

Infinity Body Splash Deo Colônia 200ml \u2013 Sofisticada e duradoura, com notas florais e amadeiradas. Elegante e versátil.

MAIS SOBRE O KIT

Todos os produtos Wepink possuem fórmula vegana e cruelty-free, com perfumação de longa duração. Um kit completo para quem ama variedade, autocuidado e fragrâncias que acompanham todos os momentos."""

content = content.replace(old_desc_0, new_desc_0)

# Replace features for product 0
content = content.replace('"01 Dream Amor No Ar Body Splash 200ml","01 Dream Viagem Encantada Body Splash 200ml","01 Dream Espelho Secreto Body Splash 200ml","01 Dream Jardim dos Mistérios Body Splash 200ml","01 Dream Filtro dos Sonhos Body Splash 200ml","01 Dream Céu de Baunilha Body Splash 200ml","01 Dream Banho de Sorte Body Splash 200ml","01 Dream Doce Tarde Body Splash 200ml"',
                          '"01 Bloquinho da Vivibora VF Deo Colônia 100ml","01 Body Splash Liberté Deo Colônia 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash Deo Colônia 200ml"')

# Replace reviews for product 0
content = content.replace('8 fragrâncias maravilhosas! Cada uma tem sua personalidade. Amei ter opções para todos os momentos.',
                          'O perfume Bloquinho da Vivibora é incrível e os body splashes são maravilhosos! Kit perfeito!')
content = content.replace('O melhor custo-benefício! São 8 body splashes lindos por um preço incrível.',
                          'Amei o kit! O Bloquinho da Vivibora é sofisticado e os 5 body splashes são deliciosos.')
content = content.replace('A linha Dream é simplesmente perfeita. Meu favorito é o Céu de Baunilha!',
                          'Cada fragrância tem sua personalidade. Uso o Obsessed para sair e o Liberté no dia a dia!')
content = content.replace('Dei de presente para minha mãe e ela amou! Agora ela tem opção para cada ocasião.',
                          'Dei de presente para minha mãe e ela amou! 6 fragrâncias lindas da Wepink.')
content = content.replace('Qualidade Wepink em 8 fragrâncias! Não tem como errar com esse kit.',
                          'Qualidade Wepink em cada produto! O RED é meu body splash favorito de todos.')

# ============================================================
# PRODUCT 1 - Kit Bloquinho da Vivibora VF Bloom e 5 Body Splash (slug: kit-nuvem-de-alegria)
# ============================================================

old_desc_1_part = "BODY SPLASH DESODORANTE COLÔNIA CUIDE-SE BEM NUVEM DE ALEGRIA 200ML"
new_desc_1 = """O Kit Bloquinho da Vivibora VF Bloom Wepink é uma edição especial que traz o perfume Bloquinho da Vivibora VF Bloom junto com 5 body splashes exclusivos. Uma combinação perfeita de fragrâncias florais e sofisticadas para todos os momentos.

ITENS INCLUSOS NO KIT

Bloquinho da Vivibora VF Bloom Deo Colônia 100ml \u2013 Fragrância floral delicada e feminina, com notas de flores frescas, peônia e um toque de musk. Perfeita para quem ama suavidade e elegância.

Body Splash Liberté Deo Colônia 200ml \u2013 Floral fresca e sofisticada, com notas de flores brancas e um toque cítrico.

Body Splash Deo Colônia 200ml \u2013 A fragrância clássica da Wepink, com notas florais e frutais envolventes.

Obsessed Deo Colônia 200ml \u2013 Intensa e marcante, com notas de amora, cereja e maçã.

RED Deo Colônia 200ml \u2013 Vibrante e apaixonante, com notas de frutas vermelhas e cacau.

Infinity Body Splash Deo Colônia 200ml \u2013 Sofisticada e duradoura, com notas florais e amadeiradas.

Todos os produtos Wepink possuem fórmula vegana e cruelty-free."""

# Find the full old description for product 1 - it starts with BODY SPLASH DESODORANTE and ends before the features
# Let's use a different approach - replace from a unique start to a unique end
content = content.replace(
    "BODY SPLASH DESODORANTE COLÔNIA CUIDE-SE BEM NUVEM DE ALEGRIA 200ML\\nO Body Splash Desodorante Colônia Cuide-se Bem Nuvem de Alegria chegou para dar aquela levantada no seu astral!",
    "O Kit Bloquinho da Vivibora VF Bloom Wepink é uma edição especial que traz o perfume Bloquinho da Vivibora VF Bloom junto com 5 body splashes exclusivos."
)

# Actually, let me try a different approach for the long descriptions
# I'll replace unique sentences within descriptions

# Product 1 description replacements
content = content.replace('BODY SPLASH DESODORANTE COLÔNIA CUIDE-SE BEM NUVEM DE ALEGRIA 200ML', 'BLOQUINHO DA VIVIBORA VF BLOOM DEO COLÔNIA 100ML')
content = content.replace('O Body Splash Desodorante Colônia Cuide-se Bem Nuvem de Alegria chegou para dar aquela levantada no seu astral!', 'Fragrância floral delicada e feminina, com notas de flores frescas, peônia e um toque de musk.')
content = content.replace('Com uma fragrância frutal cítrica que promove sensação de felicidade*, inspira ao seu redor uma verdadeira nuvem de alegria! Para todos os momentos do seu dia, é seu aliado no ritual de autocuidado, deixando a pele perfumada.', 'Perfeita para quem ama suavidade e elegância, é o perfume ideal para o dia a dia.')
content = content.replace('LOÇÃO DESODORANTE CORPORAL ILUMINADORA CUIDE-SE BEM NUVEM DE ALEGRIA 150ML', 'BODY SPLASH LIBERTÉ DEO COLÔNIA 200ML')
content = content.replace('A Loção Desodorante Iluminadora Corporal Cuide-se Bem Nuvem de Alegria chegou para dar aquela levantada no seu astral! Hidratante com brilho para deixar sua pele iluminada, entrega uma fragrância frutal cítrica que promove sensação de felicidade.', 'Floral fresca e sofisticada, com notas de flores brancas e um toque cítrico. Transmite leveza e feminilidade.')
content = content.replace('ÓLEO HIDRATANTE CORPORAL CUIDE-SE BEM NUVEM DE ALEGRIA 110ML', 'BODY SPLASH DEO COLÔNIA 200ML')
content = content.replace('O Óleo Hidratante Corporal Cuide-se Bem Nuvem de Alegria chegou para dar aquela levantada no seu astral! O primeiro e único óleo corporal de Cuide-se Bem Wepink, entrega pele aveludada como nuvem.', 'A fragrância clássica da Wepink em formato body splash. Notas florais e frutais suaves e envolventes para qualquer ocasião.')
content = content.replace('LOÇÃO HIDRATANTE DESODORANTE CORPORAL CUIDE-SE BEM NUVEM DE ALEGRIA 400ML', 'OBSESSED DEO COLÔNIA 200ML')
content = content.replace('A Loção Hidratante Desodorante Corporal Cuide-se Bem Nuvem de Alegria chegou para dar aquela levantada no seu astral! Com textura cremosa como nuvem, entrega uma fragrância frutal cítrica que promove sensação de felicidade.', 'Fragrância intensa e marcante, com notas de amora, cereja e maçã. Para quem gosta de ousar e deixar sua marca.')
content = content.replace('KIT SABONETES SORTIDOS CUIDE-SE BEM NUVEM DE ALEGRIA 4X80G', 'RED DEO COLÔNIA 200ML')
content = content.replace('O Kit Sabonetes Sortidos Cuide-se Bem Nuvem de Alegria chegou para dar aquela levantada no seu astral! Com uma fragrância frutal cítrica que promove sensação de felicidade.', 'Fragrância vibrante e apaixonante, com notas de frutas vermelhas, avelã, cacau e castanha da Índia.')
content = content.replace('SABONETE LÍQUIDO CORPORAL CUIDE-SE BEM NUVEM DE ALEGRIA 150ML', 'INFINITY BODY SPLASH DEO COLÔNIA 200ML')
content = content.replace('O Sabonete Líquido Corporal Cuide-se Bem Nuvem de Alegria chegou para dar aquela levantada no seu astral e brilho para um banho iluminado!', 'Fragrância sofisticada e duradoura, com notas florais e amadeiradas. Elegante e versátil.')
content = content.replace('Nenhum produto Wepink é testado em animais, ou seja, este item possui selo Cruelty Free. Produto vegano.', 'Todos os produtos Wepink possuem fórmula vegana e cruelty-free, com perfumação de longa duração.')

# Product 1 features
content = content.replace('"01 Body Splash Desodorante Colônia 200ml","01 Loção Desodorante Corporal Iluminadora 150ml","01 Óleo Hidratante Corporal 110ml","01 Loção Hidratante Desodorante Corporal 400ml","04 Sabonetes Sortidos 80g cada","01 Sabonete Líquido Corporal 150ml"',
                          '"01 Bloquinho da Vivibora VF Bloom Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 1 reviews
content = content.replace('O Kit Perfect Pear é simplesmente perfeito! A fragrância é suave e deliciosa, dura o dia todo.',
                          'O Bloom é uma fragrância floral divina! Combinado com os 5 body splashes, é o kit perfeito!')
content = content.replace('Dei de presente para minha mãe e ela adorou! A embalagem é linda e os produtos são de altíssima qualidade.',
                          'Dei de presente para minha mãe e ela adorou! O Bloom é delicado e os body splashes são incríveis.')
content = content.replace('Não consigo mais ficar sem! A fragrância frutal é viciante e deixa a pele super macia.',
                          'Não consigo mais ficar sem! O Liberté é meu body splash favorito do kit.')
content = content.replace('Já comprei 3 vezes! O hidratante é incrível e o body splash tem fixação excelente.',
                          'Já comprei 2 vezes! O perfume Bloom é sofisticado e os body splashes fixam muito bem.')
content = content.replace('Cuide-se Bem sempre entrega qualidade. Esse kit Nuvem de Alegria superou todas as expectativas!',
                          'Wepink sempre entrega qualidade. Esse kit do Bloom superou todas as expectativas!')

# ============================================================
# PRODUCT 2 - Kit Merry Christmas e 5 Body Splash (slug: kit-celebre-sua-forca)
# ============================================================

content = content.replace('Amor de mãe é símbolo de força e persistência. O Kit Presente Dia das Mães Celebre Sua Força celebra esse amor que transborda, com dois itens de perfumação, hidratação e cuidado diário, embalados em uma caixa especial:',
                          'O Kit Merry Christmas Wepink é a edição especial de Natal que combina o perfume Merry Christmas com 5 body splashes exclusivos. Uma coleção festiva e encantadora:')
content = content.replace('DESODORANTE COLÔNIA\\nCelebre Sua Força Feminino Desodorante Colônia traz uma fragrância floral, fresca e potente, para lembrar do quanto é importante celebrar o amor nas pequenas conquistas do dia a dia. Esse Floral Frutal carrega a potência das flores brancas e das frutas em uma perfumação que explode, cheia de frescor.',
                          'MERRY CHRISTMAS DEO COLÔNIA 100ML\\nFragrância festiva e envolvente, com notas de frutas vermelhas, especiarias e baunilha. Perfeita para celebrar momentos especiais com elegância e alegria.')
content = content.replace('Família Olfativa: Floral Frutal.', 'Família Olfativa: Frutal Especiado.')
content = content.replace('LOÇÃO CORPORAL\\nA Loção Hidratante Desodorante Corporal Celebre Sua Força traz uma fórmula que absorve de forma rápida na pele, hidratando intensamente e desodorizando o corpo. O resultado é uma pele hidratada e macia.',
                          '5 BODY SPLASHES EXCLUSIVOS\\nO kit acompanha os 5 body splashes mais desejados da Wepink: Liberté, Body Splash clássico, Obsessed, RED e Infinity. Fragrâncias para todos os estilos e momentos.')
content = content.replace('CAIXA PARA PRESENTE\\nA Caixa de Presente Wepink vem com o tamanho ideal para acomodar os produtos com segurança. Sofisticada e minimalista, as flores estampam a embalagem em 3D, representando o amor abundante que se encaixa em toda a área do presente.',
                          'EMBALAGEM ESPECIAL\\nO kit vem em uma embalagem exclusiva de Natal, perfeita para presentear.')
content = content.replace('Dimensões: 14 x 5,4 x 18,6 cm', '')
content = content.replace('MAIS PRESENTE\\nVocê compra um presente, sua pessoa especial ganha dois! Como funciona? Dentro de cada kit tem uma tag com um QR Code que dá acesso ao site exclusivo. Neste site, a presenteada escolhe um presente extra e recebe um voucher para resgatá-lo.\\n\\nNo Dia das Mães 2025, surpreenda a sua pessoa especial com a Wepink!',
                          'Todos os produtos Wepink possuem fórmula vegana e cruelty-free.')
content = content.replace('Nenhum produto Wepink é testado em animais, ou seja, este item possui selo Cruelty Free.', 'Surpreenda quem você ama com a Wepink!')

# Product 2 features
content = content.replace('"01 Celebre Sua Força Feminino Desodorante Colônia 100ml","01 Loção Desodorante Hidratante Corporal 200ml"',
                          '"01 Merry Christmas Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 2 reviews
content = content.replace('Dei para minha mãe no Dia das Mães e ela amou! A caixa é linda e o cheiro é maravilhoso.',
                          'O perfume Merry Christmas é encantador! Cheiro festivo e os body splashes complementam perfeitamente.')
content = content.replace('O kit Celebre é simplesmente perfeito. A colônia tem fixação excelente e a loção hidrata muito bem.',
                          'O kit Merry Christmas é simplesmente perfeito. A colônia é sofisticada e os body splashes são divinos.')
content = content.replace('Comprei para mim mesma e não me arrependo. Cheiro sofisticado e duradouro!',
                          'Comprei para mim mesma e não me arrependo. 6 fragrâncias maravilhosas da Wepink!')
content = content.replace('A embalagem é um charme e os produtos são de ótima qualidade. Wepink sempre entrega!',
                          'A embalagem de Natal é um charme e os produtos são de ótima qualidade. Wepink sempre entrega!')
content = content.replace('Excelente custo-benefício. Os dois produtos são incríveis e a caixa é perfeita para presente.',
                          'Excelente custo-benefício. O perfume e os 5 body splashes são incríveis para presente!')

# ============================================================
# PRODUCT 3 - Kit VF Aqua e 5 Body Splash (slug: kit-deleite)
# ============================================================

content = content.replace('O Kit Presente Cuide-se Bem Deleite traz uma fragrância doce e inesquecível, ideal para a rotina de cuidados. Para deixar tudo mais especial, o kit vem pronto para presentear em uma caixa para presente que transmite cuidado em cada detalhe, para uma lembrança especial:',
                          'O Kit VF Aqua Wepink traz o refrescante perfume VF Aqua junto com 5 body splashes exclusivos. Uma combinação perfeita de frescor e sofisticação:')
content = content.replace('BODY SPLASH\\nO Body Splash Cuide-Se Bem Deleite prolonga a sensação de frescor pós-banho com sua fragrância leve e suave.\\nA fragrância gourmand traz na saída anis fresco estrelado, aliado ao coração com frésia, flor de caramelo, orquídea, marshmallow de ouro, chantilly e vanilla. Por fim, a base é composta por benjoim, sândalo, ambrette, creme de baunilha, cedro cremoso e fluffy musk.',
                          'VF AQUA DEO COLÔNIA 100ML\\nFragrância aquática e refrescante, com notas cítricas, marinhas e um toque de musk. Ideal para quem busca frescor e leveza no dia a dia. Perfeita para o verão e momentos de descontração.')
content = content.replace('LOÇÃO CORPORAL\\nA Loção Desodorante Hidratante Corporal Cuide-se Bem Deleite confere até 48 horas de hidratação e perfumação do jeito que a gente gosta. Sua textura é absorvida rapidamente pela pele e também desodoriza o corpo.',
                          '5 BODY SPLASHES EXCLUSIVOS\\nO kit acompanha os 5 body splashes mais desejados da Wepink: Liberté, Body Splash clássico, Obsessed, RED e Infinity. Fragrâncias versáteis para todos os momentos.')
content = content.replace('CREME PARA MÃOS\\nCom a mesma perfumação da linha, o Creme para Mãos Hidratante Desodorante Cuide-se Bem Deleite hidrata intensamente mãos e cotovelos por até 30 horas.',
                          'MAIS SOBRE O KIT\\nTodos os produtos Wepink possuem fórmula vegana e cruelty-free, com perfumação de longa duração.')
content = content.replace('CAIXA PARA PRESENTE\\nA sofisticada ânfora, símbolo de Wepink, centraliza esta embalagem especial.\\nDimensões: 14,5 x 5 x 18,5 cm',
                          'Um kit completo para quem ama frescor, variedade e fragrâncias que acompanham todos os momentos.')

# Product 3 features
content = content.replace('"01 Body Splash Cuide-Se Bem Deleite 60ml","01 Hidratante Para as Mãos Cuide-Se Bem Deleite 45g","01 Loção Hidratante Desodorante Corporal Cuide-Se Bem Deleite 200ml"',
                          '"01 VF Aqua Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 3 reviews
content = content.replace('A linha Deleite é minha favorita! O cheiro de doce de leite é viciante e a hidratação é incrível.',
                          'O VF Aqua é super refrescante! Combinado com os body splashes, é o kit perfeito para o verão.')
content = content.replace('O QR Code com presente extra foi uma surpresa incrível! Wepink sempre inovando.',
                          'Os 5 body splashes são incríveis! E o VF Aqua é perfeito para o dia a dia. Wepink arrasou!')
content = content.replace('Parece sobremesa! O cheiro é doce mas não enjoativo. Perfeito para o dia a dia.',
                          'O VF Aqua é fresco e leve, perfeito para o calor. Os body splashes complementam super bem!')
content = content.replace('Dei para minha mãe e ela adorou! A caixa é linda e os produtos são de qualidade.',
                          'Presente perfeito! Meu namorado amou o VF Aqua e agora usa os body splashes todo dia.')
content = content.replace('Cuide-se Bem nunca decepciona. A linha Deleite é especialmente incrível!',
                          'Wepink nunca decepciona. O kit VF Aqua com os body splashes é sensacional!')

# ============================================================
# PRODUCT 4 - Heaven 100 ml e 5 Body Splash (slug: kit-pessegura)
# ============================================================

old_desc_4_start = 'Desfrute de uma rotina completa com 7 produtos Cuide-se Bem Doçura na Pessegura'
content = content.replace('Desfrute de uma rotina completa com 7 produtos Cuide-se Bem Doçura na Pessegura, para uma pele macia e com um cheirinho delicioso de cocada com pêssego.',
                          'O Kit Heaven Wepink traz o sofisticado perfume Heaven 100ml junto com 5 body splashes exclusivos. Uma coleção celestial de fragrâncias envolventes e femininas.')
content = content.replace('CREME HIDRATANTE DESLIZANTE\\nO Creme Hidratante Deslizante Para Lâmina Cuide-se Bem Doçura na Pessegura facilita o deslizar da lâmina durante a depilação, seja no banho ou na pele seca. Sua textura semi transparente proporciona sensação calmante na pós-depilação.',
                          'HEAVEN DEO COLÔNIA 100ML\\nFragrância floral celestial com notas de jasmim, lírio e um toque de musk branco. Sofisticada e envolvente, perfeita para mulheres que buscam elegância e delicadeza.')
content = content.replace('CREME HIDRATANTE DEPILATÓRIO CORPORAL\\nO Creme Hidratante Depilatório Corporal Cuide-se Bem Doçura na Pessegura remove os pelos de forma prática, indolor e eficiente em até 10 minutos, garantindo pele lisinha por até 5 dias.',
                          'BODY SPLASH LIBERTÉ DEO COLÔNIA 200ML\\nFloral fresca e sofisticada, com notas de flores brancas e um toque cítrico. Leveza e feminilidade para todos os momentos.')
content = content.replace('SÉRUM UNIFORMIZADOR CORPORAL\\nO Sérum Uniformizador Corporal Cuide-se Bem Doçura na Pessegura hidrata e ajuda a uniformizar o tom da pele, prevenindo e minimizando pelos encravados, ideal para uso diário em áreas específicas.',
                          'BODY SPLASH DEO COLÔNIA 200ML\\nA fragrância clássica da Wepink em formato body splash. Notas florais e frutais suaves e envolventes.')
content = content.replace('CREME ESFOLIANTE\\nO Creme Esfoliante Intenso Cuide-se Bem Doçura na Pessegura promove esfoliação intensa sem ressecar a pele, removendo células mortas e deixando a pele renovada e macia. Recomendado para uso até três vezes por semana.',
                          'OBSESSED DEO COLÔNIA 200ML\\nIntensa e marcante, com notas de amora, cereja e maçã. Para mulheres que gostam de ousar.')
content = content.replace('BODY SPLASH\\nO Body Splash Desodorante Colônia Cuide-se Bem Doçura na Pessegura traz a fragrância doce de cocada com pêssego, proporcionando frescor e perfumação ao longo do dia.',
                          'RED DEO COLÔNIA 200ML\\nVibrante e apaixonante, com notas de frutas vermelhas, avelã, cacau e castanha da Índia.')
content = content.replace('LOÇÃO CORPORAL\\nA Loção Desodorante Hidratante Cuide-se Bem Doçura na Pessegura possui textura cremosa, hidrata profundamente e perfuma a pele. Com Óleo de Coco e 97% de ingredientes de origem natural, sua fórmula é também biodegradável.',
                          'INFINITY BODY SPLASH DEO COLÔNIA 200ML\\nSofisticada e duradoura, com notas florais e amadeiradas. Elegante e versátil para qualquer ocasião.')
content = content.replace('SABONETE EM BARRA\\nOs Sabonetes em Barra Cuide-se Bem Doçura na Pessegura oferecem espuma cremosa que limpa delicadamente sem ressecar, deixando a pele perfumada e aveludada. O kit contém 4 unidades e 97% de ingredientes naturais.\\n\\nCuide-se Bem: sua pele merece este carinho!',
                          'Todos os produtos Wepink possuem fórmula vegana e cruelty-free, com perfumação de longa duração. Um kit celestial para quem ama fragrâncias sofisticadas.')

# Product 4 features
content = content.replace('"01 Creme Hidratante Deslizante Para Lâmina","01 Creme Hidratante Depilatório Corporal","01 Sérum Uniformizador Corporal","01 Creme Esfoliante Intenso","01 Body Splash Desodorante Colônia","01 Loção Desodorante Hidratante Corporal","04 Sabonetes em Barra"',
                          '"01 Heaven Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 4 reviews
content = content.replace('A Doçura na Pessegura é minha linha favorita! O cheiro de pêssego é suave e sofisticado.',
                          'O Heaven é divino! Fragrância celestial e os 5 body splashes são perfeitos para variar no dia a dia.')
content = content.replace('O sérum uniformizador mudou minha pele! E o cheirinho então... simplesmente perfeito.',
                          'O Heaven é simplesmente perfeito! Fragrância sofisticada e os body splashes complementam demais.')
content = content.replace('Cada produto é melhor que o outro. Os sabonetes são super cremosos!',
                          'Cada fragrância é melhor que a outra! O Heaven com os body splashes é uma combinação incrível.')
content = content.replace('Com 7 itens, dá pra ter uma rotina completa de cuidados. O esfoliante é sensacional!',
                          'Com 6 fragrâncias, tenho opção para cada momento! O RED é meu favorito do kit.')
content = content.replace('Investimento que vale cada centavo. A qualidade Wepink é incomparável.',
                          'Investimento que vale cada centavo. O Heaven é luxuoso e os body splashes são de qualidade top.')

# ============================================================
# PRODUCT 5 - Obsessed 100 ml e 5 Body Splash (slug: combo-chocolate)
# ============================================================

content = content.replace('O Kit One Touch traz quatro itens com o cheirinho do seu doce preferido através das linhas Cuide-se Bem e Egeo! Ele contém desodorante colônia e suflê corporal Egeo, combinando chocolate cremoso com o brilho azedinho do morango, além da cremosidade do sabonete e do esfoliante Cuide-se Bem Deleite Chocolatudo. Confira os detalhes:',
                          'O Kit Obsessed Wepink traz o marcante perfume Obsessed 100ml junto com 5 body splashes exclusivos. Para mulheres que amam fragrâncias intensas e envolventes:')
content = content.replace('DESODORANTE COLÔNIA\\nO Egeo Choc High Desodorante Colônia te convida a curtir as experiências no modo máximo! Com cheirinho de chocolate cremoso combinado ao brilho azedinho do morango e extrato de cacau, traduz o efeito sugar high. Uma explosão de sentidos para quem vive intensamente!',
                          'OBSESSED DEO COLÔNIA 100ML\\nFragrância intensa e viciante, com notas de amora, cereja e maçã que criam uma explosão de sentidos. Para mulheres que vivem intensamente e gostam de deixar sua marca por onde passam!')
content = content.replace('SUFLÊ HIDRATANTE CORPORAL\\nO Suflê Hidratante Desodorante Corporal Egeo Choc High tem textura leve deliciosa que desodoriza a pele sem deixá-la pegajosa. Proporciona hidratação por até 48 horas, toque macio e aveludado, e uma explosão de fragrância na pele.',
                          'BODY SPLASH LIBERTÉ DEO COLÔNIA 200ML\\nFloral fresca e sofisticada, com notas de flores brancas e um toque cítrico. Perfeita para o dia a dia.')
content = content.replace('SABONETE EM BARRA\\nO Sabonete em Barra Corporal Cuide-se Bem Deleite Especial oferece uma espuma cremosa e fragrância deliciosa inspirada no chocolate*, limpando sem ressecar e deixando a pele macia e aveludada.',
                          'BODY SPLASH DEO COLÔNIA 200ML\\nA fragrância clássica da Wepink. Notas florais e frutais suaves e envolventes para qualquer ocasião.')
content = content.replace('CREME ESFOLIANTE\\nO Creme Esfoliante Cuide-se Bem Deleite Chocolatudo entrega renovação da pele com textura cremosa e fragrância inspirada no cheirinho de chocolate*. Esfolia suavemente, deixando a pele hidratada, macia e perfumada.\\n\\nNenhum produto da Wepink é testado em animais, ou seja, este item possui selo Cruelty Free.',
                          'RED DEO COLÔNIA 200ML\\nVibrante e apaixonante, com notas de frutas vermelhas e cacau.\\n\\nINFINITY BODY SPLASH DEO COLÔNIA 200ML\\nSofisticada e duradoura, com notas florais e amadeiradas.\\n\\nTodos os produtos Wepink possuem fórmula vegana e cruelty-free.')

# Product 5 features
content = content.replace('"01 Egeo Choc High Desodorante Colônia","01 Suflê Hidratante Desodorante Corporal Egeo Choc High","01 Sabonete em Barra Cuide-se Bem Deleite Especial","01 Creme Esfoliante Cuide-se Bem Deleite Chocolatudo"',
                          '"01 Obsessed Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 5 reviews
content = content.replace('É como estar em uma confeitaria! O cheiro é delicioso e a hidratação é perfeita.',
                          'O Obsessed é viciante! Fragrância intensa que recebo elogios toda vez que uso.')
content = content.replace('A colônia Egeo Choc High é viciante! Recebo elogios toda vez que uso.',
                          'O kit é perfeito! O perfume Obsessed é marcante e os body splashes são maravilhosos.')
content = content.replace('O esfoliante é cremoso e delicioso. Deixa a pele super macia e cheirosa.',
                          'Os 5 body splashes complementam perfeitamente o Obsessed. Kit incrível!')
content = content.replace('Dei para minha irmã e ela ficou apaixonada! Os produtos são maravilhosos.',
                          'Dei para minha irmã e ela ficou apaixonada! O Obsessed virou o perfume favorito dela.')
content = content.replace('O suflê hidratante é incrível! Textura leve e cheirinho que dura o dia todo.',
                          'Todas as 6 fragrâncias são incríveis! Tenho opção para cada momento do dia.')

# ============================================================
# PRODUCT 6 - Red Mirage 100 ml e 5 Body Splash (slug: kit-liz-sublime)
# ============================================================

content = content.replace('O Kit Liz Sublime é uma opção incrível para surpreender. O kit contém dois itens, de perfumaria e cuidados com o corpo, com a fragrância inconfundível de Liz, embalados em uma linda caixa especial. Confira os detalhes:',
                          'O Kit Red Mirage Wepink traz o sedutor perfume Red Mirage 100ml junto com 5 body splashes exclusivos. Uma coleção para mulheres que amam fragrâncias envolventes:')
content = content.replace('DESODORANTE COLÔNIA\\nO Liz Sublime Desodorante Colônia possui uma fragrância feminina que combina notas frutais com a base exclusiva de Laire Íris Nobre, assinatura de Liz. Ideal para mulheres sublimes que brilham todos os dias!\\nFamília Olfativa: Amadeirado Frutal.',
                          'RED MIRAGE DEO COLÔNIA 100ML\\nFragrância sedutora e misteriosa, com notas de frutas vermelhas escuras, especiarias e um toque amadeirado. Ideal para mulheres que amam fragrâncias marcantes e sensuais!\\nFamília Olfativa: Frutal Amadeirado.')
content = content.replace('LOÇÃO DESODORANTE HIDRATANTE CORPORAL\\nA Loção Desodorante Hidratante Corporal Liz Sublime traz uma textura leve que hidrata e deixa a pele macia, com um toque seco e a mesma perfumação marcante do desodorante colônia.',
                          '5 BODY SPLASHES EXCLUSIVOS\\nO kit acompanha os 5 body splashes mais desejados da Wepink: Liberté, Body Splash clássico, Obsessed, RED e Infinity. Fragrâncias versáteis para todos os momentos.')
content = content.replace('CAIXA PARA PRESENTE\\nA Caixa de Presente Wepink possui tamanho ideal para acomodar os produtos com segurança. Com design sofisticado e flores estampadas em 3D, ela representa o amor abundante de um presente especial.\\nDimensões: 21 x 21 x 7,5 cm.',
                          'MAIS SOBRE O KIT\\nTodos os produtos Wepink possuem fórmula vegana e cruelty-free, com perfumação de longa duração.')
content = content.replace('MAIS PRESENTE\\nVocê compra um presente e sua pessoa especial ganha dois! Dentro de cada kit, uma tag com QR Code dá acesso a um site exclusivo para escolher um presente extra.\\n\\nSurpreenda quem você ama com a Wepink!',
                          'Um kit completo para quem ama variedade e fragrâncias que acompanham todos os momentos.\\n\\nSurpreenda quem você ama com a Wepink!')

# Product 6 features
content = content.replace('"01 Liz Sublime Desodorante Colônia 100ml","01 Loção Desodorante Hidratante Corporal Liz Sublime 100ml","01 Caixa de Presente Wepink"',
                          '"01 Red Mirage Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 6 reviews
content = content.replace('Liz Sublime é a fragrância mais elegante da Wepink! Sofisticada e duradoura.',
                          'Red Mirage é uma fragrância sedutora e marcante! Os body splashes complementam perfeitamente.')
content = content.replace('A caixa é linda e os produtos são incríveis. Minha mãe amou!',
                          'O kit é incrível! O Red Mirage é envolvente e os 5 body splashes são maravilhosos.')
content = content.replace('A fixação é excelente! O perfume dura o dia inteiro e a loção complementa perfeitamente.',
                          'A fixação do Red Mirage é excelente! Dura o dia inteiro. Os body splashes são ótimos também.')
content = content.replace('Para quem gosta de fragrâncias florais sofisticadas, é perfeito!',
                          'Para quem gosta de fragrâncias sensuais e marcantes, é o kit perfeito!')
content = content.replace('O kit é lindo e a qualidade dos produtos é impecável. Recomendo muito!',
                          'O kit Red Mirage com os body splashes é impecável. Recomendo muito!')

# ============================================================
# PRODUCT 7 - Queen Pink 100ml e 5 Body Splash (slug: kit-lily)
# ============================================================

content = content.replace('O Kit Lily é a escolha perfeita para surpreender com elegância, carinho e sofisticação. Ele traz dois itens clássicos embalados em uma linda caixa especial. Confira:',
                          'O Kit Queen Pink Wepink traz o elegante perfume Queen Pink 100ml junto com 5 body splashes exclusivos. Para mulheres que exalam sofisticação e feminilidade:')
content = content.replace('EAU DE PARFUM\\nO Lily Eau De Parfum combina a delicadeza de notas florais com a intensidade das madeiras, resultando em uma fragrância feminina sofisticada. Sua assinatura olfativa é marcada pelo exclusivo óleo essencial da flor de Lírio, obtido pelo raro processo de Enfleurage.\\nFamília Olfativa: Floral Bouquet',
                          'QUEEN PINK DEO COLÔNIA 100ML\\nFragrância floral sofisticada com notas de rosa, peônia e jasmim, combinadas com um toque de musk e sândalo. Feminina e elegante, perfeita para mulheres que buscam uma fragrância atemporal.\\nFamília Olfativa: Floral Sofisticado')
content = content.replace('CREME HIDRATANTE DESODORANTE ACETINADO\\nO Creme Acetinado Hidratante Desodorante Corporal Lily entrega a fragrância icônica de Lily em uma textura aveludada. Sua fórmula, enriquecida com Manteiga de Karité e Vitamina E, proporciona hidratação intensa por até 48 horas e protege a pele com rápida absorção.',
                          '5 BODY SPLASHES EXCLUSIVOS\\nO kit acompanha os 5 body splashes mais desejados da Wepink: Liberté, Body Splash clássico, Obsessed, RED e Infinity. Fragrâncias para todos os estilos e momentos do seu dia.')
content = content.replace('CAIXA PARA PRESENTE\\nA Caixa de Presente Wepink possui tamanho ideal para acomodar os produtos com segurança. Com design sofisticado e flores em relevo 3D, transmite amor e cuidado em cada detalhe. Feita em material rígido, pode ser reutilizada como porta-objetos.\\nDimensões: 21 x 21 x 10,5 cm',
                          'MAIS SOBRE O KIT\\nTodos os produtos Wepink possuem fórmula vegana e cruelty-free, com perfumação de longa duração.')
content = content.replace('MAIS PRESENTE\\nVocê compra um presente e sua pessoa especial ganha dois! Dentro de cada kit há um QR Code exclusivo que permite escolher um presente extra e resgatar um voucher especial.\\n\\nSurpreenda quem você ama com a Wepink!',
                          'Um kit completo para quem ama sofisticação e fragrâncias que acompanham todos os momentos.\\n\\nSurpreenda quem você ama com a Wepink!')

# Product 7 features
content = content.replace('"01 Lily Eau De Parfum 75ml","01 Creme Acetinado Hidratante Desodorante Corporal Lily 250g"',
                          '"01 Queen Pink Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 7 reviews
content = content.replace('Lily é um clássico atemporal! O perfume é simplesmente divino e o creme é luxuoso.',
                          'Queen Pink é simplesmente divino! Fragrância elegante e os body splashes são maravilhosos.')
content = content.replace('Minha mãe chorou de emoção quando ganhou! A caixa é maravilhosa e os produtos são perfeitos.',
                          'Minha mãe amou o kit! O Queen Pink é sofisticado e os 5 body splashes são perfeitos.')
content = content.replace('Lily é a fragrância da minha vida! Uso há anos e nunca canso.',
                          'Queen Pink virou minha fragrância favorita! Sofisticada e feminina, combina com tudo.')
content = content.replace('Vale cada centavo! A qualidade é impecável e a apresentação é de tirar o fôlego.',
                          'Vale cada centavo! O Queen Pink e os 5 body splashes juntos são imbatíveis.')
content = content.replace('O creme acetinado deixa a pele incrível e o cheiro combina perfeitamente com o perfume.',
                          'Todas as 6 fragrâncias são incríveis! O Queen Pink é elegante e os body splashes são versáteis.')

# ============================================================
# PRODUCT 8 - The Sunny 75 ml e 5 Body Splash (slug: kit-floratta-red)
# ============================================================

content = content.replace('O Kit Floratta Red é inspirado na delicadeza da Flor da Maçã de Vermont, trazendo a clássica fragrância da linha, além de cuidar da pele com hidratação e perfumação. São três itens da linha e um nécessaire exclusivo embalados em uma caixa especial. Confira:',
                          'O Kit The Sunny Wepink traz o radiante perfume The Sunny 75ml junto com 5 body splashes exclusivos. Uma coleção vibrante e ensolarada para mulheres que iluminam qualquer ambiente:')
content = content.replace('DESODORANTE COLÔNIA\\nO Floratta Red Desodorante Colônia combina a delicadeza da flor da maçã com a doçura da fruta, trazendo uma fragrância floriental frutal envolvente. Suas notas se abrem com frutas vermelhas, laranja e maçã, evoluem para flor de laranjeira, tuberosa, violeta, flor de lótus e flor do beijo, e finalizam com chocolate amargo, musk, sândalo, cedro e âmbar.\\nFamília Olfativa: Floriental Frutal',
                          'THE SUNNY DEO COLÔNIA 75ML\\nFragrância solar e vibrante, com notas cítricas de bergamota e laranja, combinadas com flores tropicais e um toque de vanilla. Perfeita para mulheres que irradiam energia positiva e alegria.\\nFamília Olfativa: Cítrico Floral')
content = content.replace('ÓLEO PERFUMADO\\nO Óleo Perfumado Desodorante Corporal Floratta Red proporciona uma pele perfumada e uma experiência deliciosa na hora do banho, trazendo a fragrância envolvente da linha.',
                          'BODY SPLASH LIBERTÉ DEO COLÔNIA 200ML\\nFloral fresca e sofisticada, com notas de flores brancas e um toque cítrico.')
content = content.replace('CREME HIDRATANTE DESODORANTE CORPORAL\\nO Creme Hidratante Desodorante Corporal Floratta Red hidrata intensamente por até 48 horas e perfuma a pele com toque aveludado, perfeito para quem ama a fragrância floral.',
                          'BODY SPLASH DEO COLÔNIA 200ML\\nA fragrância clássica da Wepink. Notas florais e frutais suaves e envolventes.')
content = content.replace('NÉCESSAIRE BRANCO\\nO Nécessaire Branco Off White Wepink é compacto, elegante e ideal para levar itens essenciais na bolsa ou mochila, complementando o presente com charme e praticidade.\\nDimensões: 23,4 x 12 x 14 cm',
                          'OBSESSED DEO COLÔNIA 200ML\\nIntensa e marcante, com notas de amora, cereja e maçã.')
content = content.replace('CAIXA PARA PRESENTE\\nA Caixa de Presente Wepink possui tamanho ideal para acomodar os produtos com segurança. Com design sofisticado e flores estampadas em 3D, é feita em material rígido, ideal para ser reaproveitada como porta-objetos.\\nDimensões: 30 x 21 x 8,3 cm',
                          'RED DEO COLÔNIA 200ML\\nVibrante e apaixonante, com notas de frutas vermelhas, avelã e cacau.')
content = content.replace('MAIS PRESENTE\\nVocê compra um presente e sua pessoa especial ganha dois! Cada kit contém um QR Code exclusivo que permite escolher um presente extra para resgate.\\n\\nSurpreenda a sua pessoa especial com a Wepink!',
                          'INFINITY BODY SPLASH DEO COLÔNIA 200ML\\nSofisticada e duradoura, com notas florais e amadeiradas.\\n\\nTodos os produtos Wepink possuem fórmula vegana e cruelty-free.')

# Product 8 features
content = content.replace('"01 Floratta Red Desodorante Colônia 75ml","01 Creme Hidratante Desodorante Corporal Floratta Red 200ml","01 Óleo Perfumado Desodorante Corporal Floratta Red 150ml","01 Nécessaire Branco Off White Wepink"',
                          '"01 The Sunny Deo Colônia 75ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 8 reviews
content = content.replace('Floratta Red é intensa e marcante! A nécessaire é um bônus incrível.',
                          'The Sunny é radiante e alegre! Os 5 body splashes complementam perfeitamente o kit.')
content = content.replace('Com 4 produtos, a fragrância fica muito mais duradoura. Amei a combinação!',
                          'Com 6 fragrâncias, tenho opção para cada momento! The Sunny é meu favorito.')
content = content.replace('A caixa é linda e a nécessaire é super útil. Minha mãe adorou!',
                          'O kit é lindo! The Sunny é perfeito para o dia a dia e os body splashes são incríveis.')
content = content.replace('Para quem gosta de fragrâncias marcantes, é perfeito! A fixação é excelente.',
                          'O The Sunny é vibrante e alegre! Fixação excelente e os body splashes são ótimos.')
content = content.replace('O óleo perfumado é divino e deixa a pele super macia e cheirosa.',
                          'Todas as fragrâncias do kit são divinas! O The Sunny com os body splashes é combo perfeito.')

# ============================================================
# PRODUCT 9 - Fatal Black 100 ml e 5 Body Splash (slug: kit-chocolatudo)
# ============================================================

content = content.replace('O Kit Celebrate Life te convida a mergulhar em doces momentos de autocuidado! Com produtos das linhas Cuide-se Bem e Intense, este combo proporciona uma rotina completa com o cheirinho irresistível de chocolate*. Confira os detalhes:',
                          'O Kit Fatal Black Wepink traz o intenso perfume Fatal Black 100ml junto com 5 body splashes exclusivos. Para mulheres que amam fragrâncias poderosas e marcantes:')
content = content.replace('LOÇÃO CORPORAL 400ML\\nA Loção Desodorante Hidratante Corporal Cuide-se Bem Deleite Chocolatudo entrega hidratação intensa, textura cremosa e fragrância inspirada no chocolate. Deixa a pele macia, perfumada e protegida por até 48 horas.',
                          'FATAL BLACK DEO COLÔNIA 100ML\\nFragrância intensa e poderosa, com notas de pimenta preta, couro e um toque de vanilla escura. Sensual e misteriosa, perfeita para mulheres que deixam sua marca por onde passam.')
content = content.replace('BODY SPLASH\\nO Body Splash Desodorante Colônia Cuide-se Bem Deleite Chocolatudo prolonga a sensação de frescor pós-banho com fragrância deliciosa e refrescante, ideal para levar na bolsa.',
                          'BODY SPLASH LIBERTÉ DEO COLÔNIA 200ML\\nFloral fresca e sofisticada, com notas de flores brancas e um toque cítrico.')
content = content.replace('CREME ESFOLIANTE\\nO Creme Esfoliante Cuide-se Bem Deleite Chocolatudo renova a pele sem agredir, com textura cremosa e cheirinho de chocolate, deixando a pele macia, hidratada e perfumada.',
                          'BODY SPLASH DEO COLÔNIA 200ML\\nA fragrância clássica da Wepink. Notas florais e frutais suaves e envolventes.')
content = content.replace('SABONETE EM BARRA\\nO Sabonete em Barra Corporal Cuide-se Bem Deleite Especial oferece espuma cremosa e fragrância deliciosa inspirada no chocolate. Limpa a pele suavemente, deixando-a macia e aveludada.',
                          'OBSESSED DEO COLÔNIA 200ML\\nIntensa e marcante, com notas de amora, cereja e maçã.')
content = content.replace('GLOSS LABIAL MARROM\\nO Gloss Labial Marrom Intense Deleite Chocolatudo entrega um toque de cor marrom com efeito super glossy. Fórmula hidratante, não pegajosa e com aroma irresistível de chocolate.',
                          'RED DEO COLÔNIA 200ML\\nVibrante e apaixonante, com notas de frutas vermelhas, avelã e cacau.')
content = content.replace('GLOSS LABIAL ROSA\\nO Gloss Labial Rosa Intense Deleite Chocolatudo proporciona um toque de cor rosa, brilho intenso, hidratação e cheirinho de chocolate.',
                          'INFINITY BODY SPLASH DEO COLÔNIA 200ML\\nSofisticada e duradoura, com notas florais e amadeiradas.')
content = content.replace('PALETA DE MAQUIAGEM MULTIFUNCIONAL\\nA Paleta de Maquiagem Multifuncional Cuide-se Bem Chocolatudo traz 8 cores versáteis para criar looks incríveis para olhos e rosto. Com textura macia e aplicação fácil.',
                          'MAIS SOBRE O KIT\\nTodos os produtos Wepink possuem fórmula vegana e cruelty-free, com perfumação de longa duração.')
content = content.replace('LOÇÃO CORPORAL 200ML\\nA versão viagem da Loção Desodorante Hidratante Corporal Cuide-se Bem Deleite Chocolatudo é perfeita para o dia a dia, mantendo a pele hidratada e perfumada onde você estiver.\\n\\n*Fragrância inspirada no cheirinho de chocolate.',
                          'Um kit poderoso para quem ama fragrâncias intensas e marcantes.')

# Product 9 features
content = content.replace('"01 Loção Desodorante Hidratante Corporal 400ml","01 Body Splash Desodorante Colônia","01 Creme Esfoliante","01 Sabonete em Barra Deleite Especial","01 Gloss Labial Marrom Intense","01 Gloss Labial Rosa Intense","01 Paleta de Maquiagem Multifuncional","01 Loção Desodorante Hidratante Corporal 200ml"',
                          '"01 Fatal Black Deo Colônia 100ml","01 Body Splash Liberté 200ml","01 Body Splash Deo Colônia 200ml","01 Obsessed Deo Colônia 200ml","01 RED Deo Colônia 200ml","01 Infinity Body Splash 200ml"')

# Product 9 reviews
content = content.replace('A paleta de sombras é linda e o lip gloss tem um cheirinho incrível de chocolate!',
                          'O Fatal Black é uma fragrância poderosa! Marcante e sensual. Os body splashes completam o kit.')
content = content.replace('Finalmente um kit que combina skincare e maquiagem! Os produtos são maravilhosos.',
                          'O kit Fatal Black é incrível! O perfume é intenso e os 5 body splashes são maravilhosos.')
content = content.replace('Parece uma doceria! O body splash é viciante e dura bastante.',
                          'O Fatal Black é viciante! Fragrância intensa que dura o dia todo.')
content = content.replace('Com 8 itens, dá pra curtir muito! O esfoliante deixa a pele super macia.',
                          'Com 6 fragrâncias diferentes, tenho opção para cada ocasião. Kit sensacional!')
content = content.replace('O custo-benefício é excelente. Todos os produtos são de alta qualidade.',
                          'O custo-benefício é excelente. O Fatal Black e os body splashes são de alta qualidade.')

with open('assets/index-WKGCUSBO.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Todas as descrições e reviews foram atualizadas com sucesso!")
