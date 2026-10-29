# Ambiente

Verificado em **2026-10-29** no ambiente de nuvem do Claude Code
(contêiner Linux, 4 CPUs, 15 GB de RAM, sem GPU). O contêiner é temporário:
o que não for commitado e enviado ao GitHub se perde.

## Ferramentas

| Ferramenta | Disponível | Versão |
|---|---|---|
| ffmpeg / ffprobe | sim | 6.1.1 |
| Python | sim | 3.13.17 (pip 24.0; numpy e pillow instalados) |
| Node.js | sim | v22.22.0 (npm 10.9.4) |
| ImageMagick (`convert`) | sim | 6.9.12 |
| MediaPipe (recorte de pessoa) | sim, em venv fora do repo | 1.2.0 (Google, Apache 2.0); modelo `selfie_segmenter.tflite` baixado de storage.googleapis.com |
| libegl1, libgles2, libgl1 (apt) | sim | necessárias para o MediaPipe |
| yt-dlp, sox, whisper, moviepy | não | — |

### Recursos do ffmpeg confirmados
- Codificadores: libx264, libx265, libvpx/VP9, aac, libmp3lame, libopus.
- Filtros: `crop`, `scale`, `xfade`, `afade`, `loudnorm`, `drawtext`,
  `subtitles`/`ass` (com libass, freetype, fontconfig e fribidi — legendas com acento funcionam).
- Teste real feito: vídeo 1920x1080 → recorte 9:16 (1080x1920) + legenda queimada
  (fonte Inter) + áudio normalizado com `loudnorm`. Funcionou.

### Fontes instaladas (119)
Inclui Inter, DejaVu Sans/Serif, FreeSans, Carlito, Caladea, entre outras.

## Acesso à internet

A rede passa por um proxy com política restrita. Teste feito com `curl`:

| Site | Acesso |
|---|---|
| pypi.org (pip) | ✅ |
| registry.npmjs.org (npm) | ✅ |
| api.github.com / github.com / raw.githubusercontent.com | ✅ |
| archive.ubuntu.com (apt) | ✅ |
| storage.googleapis.com, github.com/.../releases (download de modelos) | ✅ (testado em 2026-10-29) |
| youtube.com | ❌ bloqueado |
| pixabay.com, pexels.com, mixkit.co, unsplash.com | ❌ bloqueado |
| freesound.org | ❌ bloqueado |
| fonts.google.com, huggingface.co | ❌ bloqueado |
| ffmpeg.org, archive.org, google.com, cdn.jsdelivr.net | ❌ bloqueado |

**Consequências práticas**
- Dá para instalar ferramentas via pip, npm e apt (sempre com aprovação, ver CLAUDE.md).
- Não dá para baixar músicas, vídeos de banco de imagens ou fontes direto desses sites.
  Alternativas: o Dionatan envia os arquivos pelo repositório, ou libera os domínios
  em *Network access* nas configurações do ambiente
  (https://code.claude.com/docs/en/cloud-environments#network-access).
- Modelos de transcrição automática (ex.: Whisper) normalmente baixam pesos do
  huggingface.co, que está bloqueado.

> O ambiente é temporário: o venv do MediaPipe precisa ser recriado em sessões novas.
