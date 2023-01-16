score = {
    'python': 80,
    'django': 89,
    'web': 83
}
# algorithm 성적 추가
score['algorithm'] = 90
# python 성적 정정
score['python'] = 85
# 전체 평균 점수
print(sum(score.values()) / 4)
