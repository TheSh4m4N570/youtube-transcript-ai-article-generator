import os
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi


def extract_transcript(video_id, languages=['en']):
    """
    :param video_id: The ID of the video for which the transcript needs to be extracted.
    :param languages: The languages in which the transcript should be extracted. Default is ['en'].
    :return: The extracted transcript as a normal text string.
    """
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    cleaned_data = [item.get('text', '') for item in transcript]
    normal_text = '\n'.join(cleaned_data)
    return normal_text


def save_transcript(transcript, video_id):
    """
    :param transcript: The transcript to be saved
    :param video_id: The ID of the video for which the transcript belongs
    :return: None

    Save the given transcript to a file in the 'transcripts' directory.

    The transcript is saved in a text file with a filename constructed as 'transcript_' + video_id + '_' +
        today's date in the format 'YYYY_MM_DD_HH' + '.txt'.

    If the 'transcripts' directory does not exist, it will be created.

    Example usage:
        save_transcript(transcript, 'video123')
    """
    # construct a filename with 'trancript', today's date, and current hour
    filename = 'transcript_' + video_id + '_' + datetime.now().strftime('%Y_%m_%d_%H') + '.txt'

    # ensure the transcripts directory exists
    if not os.path.exists('transcripts'):
        os.makedirs('transcripts')

    # open the file in the transcripts directory and save the transcript
    with open(os.path.join('transcripts', filename), 'w') as f:
        f.write(str(transcript))


