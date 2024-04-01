import pandas as pd

json_data = {
  "columns": ["Movie", "Release Year", "Audience", "Rating"],
  "index": [0, 1, 2, 3, 4, 5, 6, 7],
  "data": [
    ["Avengers", 2012, 1500, 8.8],
    ["Interstellar", 2014, 1100, 9.1],
    ["Frozen", 2013, 1020, 8.5],
    ["About Time", 2013, 950, 8.7],
    ["The Dark Knight", 2008, 1300, 9.0],
    ["Inception", 2010, 1200, 8.8],
    ["La La Land", 2016, 800, 8.6],
    ["Toy Story", 2010, 980, 8.5]
  ]
}

# JSON 데이터를 DataFrame으로 변환
df = pd.DataFrame(json_data['data'], columns=json_data['columns'])
print(df)

# 1) 전체 데이터 중에서 ''Moive 정보만 출력하시오.
print(df.Movie)
# 2) 전체 데이터 중에서 'Movie','Rating' 정보를 출력하시오.
print(df[['Movie','Rating']])
# 3) 2013년 이후에 개봉한 영화 데이터 중에서 'Movie','Rating' 정보를 출력하시오.
print(df.loc[df['Release Year'] > 2013, ['Movie','Rating']])
# 4) 주어진 계산식을 참고하여 'Recommend' Column을 추가하시오.
# Recommend = (Audience * Rating) // 100
df['Recommend'] = df.Audience * df.Rating // 100
print(df)
# 5) 전체 데이터를 'Release Year' 기준 내림차순으로 출력하시오.
print('============================================================')
print(df.sort_values(by='Release Year', ascending=False))
print(df.sort_values(by='Recommend', ascending=False).head(3))