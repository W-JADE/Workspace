# 다음 소스코드가 실행 되도록 해당 클래스를 구현하라.
# Music 클래스 : song, singer, play(), 생성자...
# MusicPlayer 클래스 : list,
# * typing 모듈 사용

from typing import List

class Music :
    def __init__(self, singer:str, song:str) :
        self.singer = singer
        self.song = song
    def play(self):
        print(f"{self.singer}의 {self.song} 노래 실행중...")
    
    def __str__(self) :
        return f"{self.singer}의 {self.song} 노래 실행중..."

class MusicPlayer :
    def __init__(self, music_list:List[Music]= []) :
        self.music_list:List[Music] = music_list
    
    def setList(self, music_list:List[Music]= []):
        self.music_list = music_list
        
    def play(self):
        for music in music_list :
            music.play()
   
music_list : List[Music] = [
    Music("아이유", "좋은날"),
    Music("악동뮤지션", "다리꼬지마"),
    Music("데이먼스이어", "Yours")
]

player = MusicPlayer()
player.setList(music_list)
player.play()

'''
[출력결과]
아이유의 좋은날 노래 실행중...
악동뮤지션의 다리꼬지마 노래 실행중...
데이먼스이어의 Yours 노래 실행중...
'''