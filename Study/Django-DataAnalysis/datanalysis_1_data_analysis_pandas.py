import pandas   as pd   

#Series
data = ['a','b', 'c', 'd', 'e']
se = pd.Series(data)
print(type(se))
print(se)
print(se.index)
print(se.values)
print(se[0:3])
se.name = 'abc'
se.index.name = 'index'
print(se)


# DF(DataFrame = Excel) 두 개 이상의 Series
data = {
    'country' : ['kor', 'usa', 'china', 'japan'],
    'rank' : [1,2,3,4],
    'grade': ['a', 'b', 'c', 'd']
}
print(pd.DataFrame(data)) # csv to json, json to csv, xlsx
df = pd.DataFrame(data)

#데이터 셀랙션 >> 데이터를 불러오는 방법
# (1) df.컬럼, df['컬럼']

print(df.grade)
print(df[['rank', 'country']])

# (2) df.loc[인덱스값, 컬럼명]

print(df.loc[:, 'rank'])

# 결과는 같다.
print(df.loc[df['rank'] > 2, ['country', 'grade']])
print(df[df['rank'] > 2][['country', 'grade']])

# 삭제하는 방법 (drop)
# (1) 단순하게 행 데이터를 삭제하는 방법
print(df.drop([2])) # 이 명령은 실제로 삭제하지는 않고 보여주지만 않는다. 
print(df.drop([2], inplace=True)) # inplace=True 속성을 주어야 실제로 삭제한다.

print(df)

# (2)컬럼을 삭제
# print(df.drop('rank', axis=1)) # 이 명령은 실제로 삭제하지는 않고 보여주지만 않는다. 
# print(df.drop('rank', axis=1, inplace=True)) # inplace=True 속성을 주어야 실제로 삭제한다. 
df = df.drop('rank', axis=1) # 기존의 df에 조회한 값을 덮어쓰는 방식으로 삭제도 가능하다. 
print(df)

df['rank'] = [1,2,3]    #컬럼 값 추가 가능
print(df)

#기술통계
print(df.info())
print(df.describe())


# 데이터 정렬 >> sort_index or sort_values()
df['new_rank'] = [10,100,30]
print(df)
print(df.sort_values(by='new_rank', ascending=False)) #내림차순

# null 데이터(NaN) 처리
# isnull() >> 데이터의 null 여부
# fillna() >> null 데이터를 채워주세요.
# dropna() >> null 데이터를 지워주세요.
print(df)
# df.loc[1,'grade'] = pd.NA
# print(df.isnull().sum())
df['grade'] = pd.NA
print(df)
df.fillna(value='pass', inplace=True)
print(df)
df.loc[1, 'rank'] = pd.NA
print(df)
print('============================================================')
df.dropna(how='any', inplace=True) #how = any(하나만 NA여도 지운다)/ all(모든 컬럼이 NA인 경우에 지운다)
print(df)

