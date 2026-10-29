# Registro de decisões

Formato: data — decisão — motivo. Mais recentes no topo.

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
