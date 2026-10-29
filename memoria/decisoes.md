# Registro de decisões

Formato: data — decisão — motivo. Mais recentes no topo.

## 2026-10-29 — Pasta roteiros/
- **Decisão:** criar `roteiros/` no GitHub para guardar o texto falado de cada vídeo (base da legenda).
- **Motivo:** pedido do Dionatan; a transcrição automática não funciona neste ambiente.

## 2026-10-29 — Edições pesadas ficam no computador
- **Decisão:** vídeos e áudios não vão mais para o GitHub; as edições pesadas serão feitas no computador do Dionatan.
  O repositório guarda só CLAUDE.md, INDEX.md, memoria/, scripts em `ferramentas/` e cenários leves.
- **Motivo:** vídeos deixam o repositório pesado (limite de 100 MB por arquivo).
- **Estado:** os vídeos de teste continuam no histórico do Git (cerca de 30 MB no total); não foram apagados do histórico.

## 2026-10-29 — Versão 2 do podcast: cenário frontal desenhado
- **Motivo:** o Dionatan achou a v1 ruim; o problema principal era o ângulo da foto (de lado/de baixo) diferente do vídeo (de frente).
- **Decisão:** cenário desenhado por código, de frente e na altura dos olhos, desfocado como câmera real, com luz quente; sombra dela na parede; correção de cor; grão leve.
- **Limites reconhecidos:** não é foto real; o vídeo original é 576x864. Para ficar realista de verdade: gravar vídeo novo em 1080p com luz suave e usar foto de fundo real, de frente.
- **Pendente:** Dionatan ainda não aprovou ferramentas extras (RVM, Video Cleanup). Nenhuma foi baixada.
- **Arquivos:** manter vídeos abaixo de ~50 MB (limite do GitHub é 100 MB).

## 2026-10-29 — Podcast da Taína com fundo trocado
- **Decisão:** criar um podcast com marca própria para a Taína, com ela no escritório dela
  atrás de uma mesa. Fundo trocado com recorte de pessoa (MediaPipe), fundo vindo de foto do escritório real
  enviada pelo Dionatan. Nome do podcast: provisório "Papo de Divã" (Dionatan ainda não definiu). Cargo na tarja: "Psicanalista · Apresentadora".
- **Como foi feito:** foto do escritório recortada em 9:16 e levemente desfocada; Taína recortada quadro a quadro,
  ampliada 2x e posicionada na cadeira; a parte da mesa da foto volta por cima dela (efeito "atrás da mesa");
  tarja inferior com nome e cargo; título do podcast no topo; áudio normalizado a -16 LUFS.
- **Limites:** fundo é foto de banco/ilustração enviada pelo Dionatan, não o escritório real dela, e o vídeo original é 576x864, então a imagem fica um pouco suave.
- **Aprovado pelo Dionatan:** instalar MediaPipe (pip, Apache 2.0, pacote lido antes) e baixar o modelo de segmentação do Google.
- **Nome correto:** Taína (com acento no í).

## 2026-10-29 — Estilo telejornal com marca fictícia (teste)
- **Decisão:** não recriar identidade visual de emissoras reais (Globo, SBT) nem fazer parecer
  que a Taína tem programa nelas. Estilo telejornal só com marca própria/fictícia ("Papo de Divã", nome provisório).
- **Teste feito:** vídeo 576x864 → 9:16 (1080x1920) com fundo desfocado, corte da marca SBT do
  topo, tarja com nome e profissão, áudio com loudnorm (-16 LUFS). Saída em `saida/`.
- **Motivo:** evitar conteúdo que pareça transmissão real de terceiros; o Dionatan queria testar os comandos.

## 2026-10-29 — Ritmo e legenda
- **Decisão:** ritmo calmo; legenda de frase inteira. A Taína é cliente do Dionatan.
- **Motivo:** resposta do Dionatan na entrevista de estilo.

## 2026-10-29 — Formato dos vídeos
- **Decisão:** vídeos verticais 9:16 (1080x1920), de 30 a 60 segundos, para Instagram e TikTok,
  no nicho da Taína, terapeuta psicanalista.
- **Motivo:** resposta do Dionatan na entrevista de estilo.

## 2026-10-29 — Estrutura inicial do repositório
- **Decisão:** criar `CLAUDE.md`, `INDEX.md` e a pasta `memoria/`
  (sobre-mim, estilo-de-edicao, ambiente, decisoes).
- **Motivo:** dar ao Claude contexto fixo sobre o Dionatan, o estilo dos vídeos e o ambiente.

## 2026-10-29 — Ferramenta base de edição: ffmpeg
- **Decisão:** usar o ffmpeg (já instalado, gratuito) para cortar, juntar,
  legendar, converter para 9:16 e tratar áudio.
- **Motivo:** já está no ambiente, tem todos os filtros necessários e não exige instalar nada.

## 2026-10-29 — Regras de segurança
- **Decisão:** nada de skill/agente/plugin de terceiros sem aprovação; ler o código antes
  de instalar; nunca guardar senhas ou chaves em arquivos.
- **Motivo:** pedido do Dionatan.
