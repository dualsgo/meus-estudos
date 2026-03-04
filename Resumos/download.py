from typing import Any
import yt_dlp


def baixar_video(url: str, baixar_playlist: bool = False) -> None:
    if not url.strip():
        print("URL inválida.")
        return

    opcoes: dict[str, Any] = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "noplaylist": not baixar_playlist,
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
        print("\nDownload concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar: {e}")


if __name__ == "__main__":
    link = input("Cole a URL do vídeo aqui: ").strip()
    escolha = input("Baixar playlist inteira? (s/n): ").strip().lower()
    baixar_video(link, baixar_playlist=escolha == "s")
