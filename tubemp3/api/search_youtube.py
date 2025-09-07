import yt_dlp as youtube_dl
import threading




def search_youtube(query, max_results=10):
    """Searches for music on YouTube.

    Args:
        query (str): Search query.
        max_results (int, optional): Number of search results. Defaults to 10.

    Returns:
        dict: Search results or None if an error occurs.
    """
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'format': 'bestaudio/best',
        'no_warnings': True,
        'ignoreerrors': True,
        'skip_download': True,
        'dump_single_json': True,
        'default_search': "ytmusic"
    }

    # Variável para armazenar o resultado
    result = None

    def run_search():
        nonlocal result
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
            except Exception as e:
                print(f"Error searching YouTube: {e}")
                result = None

    # Executa a busca em uma thread separada para evitar o bloqueio
    search_thread = threading.Thread(target=run_search)
    search_thread.start()
    search_thread.join()  # Aguarda a thread terminar para garantir que 'result' seja preenchido

    return result  # Retorna o resultado para ser utilizado em outro código
