import pandas as pd

# 엑셀파일 병합 및 저장(car_data.xlsx)
# files = [
#     '2020년_06월_자동차_등록자료_통계.xlsx',
#     '2021년_06월_자동차_등록자료_통계.xlsx',
#     '2022년_06월_자동차_등록자료_통계.xlsx',
#     '2023년_06월_자동차_등록자료_통계.xlsx',
#     '2024년_06월_자동차_등록자료_통계.xlsx',
#     '2025년_06월_자동차_등록자료_통계.xlsx']

# all_data = []

# for file in files :
#     try:
#         df = pd.read_excel(file, sheet_name='04.성별_연령별')
#         year = file[:4] # 파일명 앞 4글자가 연도
#         df['연도'] = year
#         all_data.append(df)
#         print(f'{year}년 데이터 읽음 {len(df)}행')
#     except :
#             print(f'{file} 읽기 실패')

# if all_data :
#     result = pd.concat(all_data, ignore_index=True)

#     # 연도 컬럼을 맨 앞으로
#     cols = ['연도'] + [col for col in result.columns if col != '연도']
#     result = result[cols]

#     result.to_excel('car_data.xlsx', index=False)
#     print(f'\n 완료! 총 {len(result)}행 저장됨')
# else : 
#     print('읽을 수 있는 파일이 없습니다.')

# car_data 구조 확인
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import koreanize_matplotlib

car_data = pd.read_excel('car_data.xlsx')
print(tabulate(car_data.head(), headers='keys', tablefmt='psql'))

# 결측치 확인
print(car_data.isna().sum())

# 결측치 채우기
car_data['gender'] = car_data['gender'].ffill()
car_data.to_excel('../PROJECT_OPENDATA_4/car_data.xlsx', index=False)

# 결측치 확인
print(car_data.isna().sum()) 

# 결측치(빈 칸) 행 삭제
car_data = car_data.dropna(axis=0)
car_data.to_excel('../PROJECT_OPENDATA_4/car_data.xlsx', index=False)

# 결측치 확인
print(car_data.isna().sum()) 

# 특정 컬럼['연령/시도'] 행 삭제
# 컬럼['연령/시도'] 컬럼에서 '법인 및 사업자' 값이 아닌 행만 남긺
car_data = car_data[car_data['age'] != '법인 및 사업자']
car_data.to_excel('../PROJECT_OPENDATA_4/car_data.xlsx', index=False)

# coloumn명 변경
car_data = pd.read_excel('car_data.xlsx', header=1)
col_names = ['Year', 'gender', 'age', 'total', 'Seoul', 'Busan', 'Daegu', 'Incheon',
             'Gwangju', 'Daejeon', 'Ulsan', 'Sejong', 'Gyeonggi', 'Gangwon', 'Chungbuk', 'Chungnam',
             'Jeonbuk', 'Jeonnam', 'Gyeongbuk', 'Gyeongnam', 'Jeju']
car_data = pd.read_excel('car_data.xlsx', header=0)
car_data.columns = col_names
car_data.to_excel('../PROJECT_OPENDATA_4/car_data.xlsx', index=False)
print(tabulate(car_data.head(), headers='keys', tablefmt='psql'))

# 데이터 불러오기
car_data = pd.read_excel('../PROJECT_OPENDATA_4/car_data.xlsx')

# 도시 컬럼 리스트
cities = ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Ulsan']

# 연도 리스트
years = [2020, 2021, 2022, 2023, 2024, 2025]

# 연령 리스트
ages = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# subplot 설정
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('2020~ 2025년 도시별 성별 차량 등록 현황', fontsize=16)

for ctiy in cities :
    male_list = []
    female_list = []  

    for row in car_data :
        if year in row[0] :
            for age in ages :
                male_list.append


# # 연도별 남녀 비율 꺾은선 그래프
# for i, city in enumerate(cities): # (0, '서울'), (1, '부산'), (2, '대구')
#     male_list = []
#     female_list = []

#     # 2차원 배열의 인덱스를 계산
#     row = i // 3
#     col = i % 3

#     # 각 도시별 남성과 여성의 차량 등록 대수 추출
#     for year in years:
#         if city in cities :
#             year_data = car_data[car_data['Year'] == year]

#         male_value = year_data[year_data['gender'] == '남성'][city].values[0]
#         female_value = year_data[year_data['gender'] == '여성'][city].values[0]

#         male_list.append(male_value)
#         female_list.append(female_value)

#     # 꺾은선 그래프 (axs[row, col] 사용)
#     axs[row, col].plot(years, male_list, 'o-', label='남성', color='skyblue', linewidth=2)
#     axs[row, col].plot(years, female_list, 's-', label='여성', color='lightpink', linewidth=2)

#     # ax 메서드로 그래프 설정
#     axs[row, col].set_title(f'{city}')
#     axs[row, col].set_xlabel('연도')
#     axs[row, col].set_ylabel('등록 수')
#     axs[row, col].legend()
#     axs[row, col].grid(True, alpha=0.3)

# plt.tight_layout()
# plt.show()