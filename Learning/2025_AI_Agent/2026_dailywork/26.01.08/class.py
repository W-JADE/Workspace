# [문제]
# 다음 소스코드가 실행 되도록 해당 클래스를 구현하라.
# Music 클래스 : song, singer, play(), 생성자...
# MusicPlayer 클래스 : list,

class Music:
    def __init__(self, singer, song):
        self.singer = singer
        self.song = song

    def play(self):
        print(f"My Music_list : {self.singer} - {self.song}")
    
class MusicPlayer :
    def __init__(self):
        self.music_list = []
    
    def setlist(self, music_list):
        self.music_list = music_list
    
    def play(self) :
        print("기분 전환을 위한 음악목록")
        for music in self.music_list:
            music.play()
     
music_list = [
    Music("아이유", "좋은날"),
    Music("악동뮤지션", "다리꼬지마"),
    Music("데이먼스이어", "Yours")
]

player = MusicPlayer()
player.setlist(music_list)
player.play()

'''
[출력결과]

기분 전환을 위한 음악목록
My Music_list : 아이유 - 좋은날
My Music_list : 악동뮤지션 - 다리꼬지마
My Music_list : 데이먼스이어 - Yours
'''