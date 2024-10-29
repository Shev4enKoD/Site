document.getElementById('downloadBtn').addEventListener('click', async () => {
    const url = document.getElementById('videoUrl').value;
    if (!url) {
        alert("Введите корректную ссылку.");
        return;
    }

    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });

        if (!response.ok) throw new Error('Ошибка при загрузке видео');

        const data = await response.json();
        const videoPlayer = document.getElementById('videoPlayer');
        const downloadLink = document.getElementById('downloadLink');

        videoPlayer.src = data.videoUrl;
        downloadLink.href = data.videoUrl;
        downloadLink.innerText = 'Скачать видео';

        document.getElementById('videoContainer').style.display = 'block';
    } catch (error) {
        alert(error.message);
    }
});
