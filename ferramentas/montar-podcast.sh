#!/usr/bin/env bash
# Monta o vídeo do podcast: recorta a pessoa (MediaPipe), coloca atrás da mesa do escritório e adiciona tarjas.
# Uso: montar-podcast.sh VIDEO.mp4 SAIDA.mp4   (precisa de bg.png/desk.png preparados com PIL e do venv do MediaPipe)
# Passos: 1) recorte-pessoa.py gera mask.mkv  2) ffmpeg compõe fundo + pessoa (escala 2.0, x=-20, y=128) + mesa por cima + tarjas.
# Detalhes completos em memoria/decisoes.md.
