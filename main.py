from Extractor import extract_transcript, save_transcript
from ai_article_writer import article_writer

if __name__ == '__main__':
    yt = extract_transcript(video_id="9AlfFkmKaS4",)
    save_transcript(transcript=yt, video_id="9AlfFkmKaS4")
    print(article_writer.generate_article(yt))
