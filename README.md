# Story-Score

Story-Score is an example project that aims at adding background scores to textual storylines.

## Examples
 
### Input Text 1

> "Oh my god, that was so scary. The ghost of Colonel Sanders was eating at my local K F C."

### Output Audio 1

[Scored Audio File](audio/output_1.mp3)

### Input Text 2

> "As Rachel was looking around, everyone was in happy spirits as they were dancing!"

### Output Audio 2

[Scored Audio File](audio/output_2.mp3)

## How does it work? 

This project utilizes models at `Huggingface Hub` and `Beatoven.ai`. See [python notebook](./main.ipynb) for more details.

![Introducing Beatoven SDK](https://github.com/SachinVarghese/story-score/assets/24502613/0c42d536-1a9e-4c44-b36c-971f02e307ad)

Story-score takes text input and utilizes a custom voice embedding to create speech audio. You can select your own embedding as needed. Also, the emotion or mood associated with the text is detected using another emotion classification model. Both these models are publicly available on the Huggingface Hub for non-commercial usage. Further, the synthesized speech duration and mood parameters are passed to the Beatoven SDK to create a track that can be utilized as a background score. Finally, the speech is combined with the composed track to create the audio with a background score. 
