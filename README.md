﻿# Crawler 모음집

<H1> OverView </H1>
<ol> 페이지 리뉴얼이나 태그 변경 시 동작 불가 </ol>
<ol> 확인 기간 : 2021.02.10 </ol>

<hr>

<H1> 오늘의 집 </H1>
<ol> 사용법 
	<ol>ohou_crawling("find_url", mode)
		<ol>mode 기준 ( 0 : 기본 / 1 : 리뷰순 정렬 후 크롤링 / 2 : 판매순 정렬 후 크롤링</ol>
	</ol>
</ol>
<ol> query="" 에 원하는 제품명 혹은 회사명 입력 시 등록 된 상품 중 보이는 범위까지 긁어옴</ol>
<ol> 스크롤 기능 추가 + 알고리즘 수정 예정
  <ol> 오늘의 집 페이지는 12개의 product만 노출=> 스크롤 이동 시, 태그 내 아이템의 수정만 이뤄짐</ol>
  <ol> 데이터 수집 이후 이전 페이지로 돌아가서 스크롤 다운으로 갱신 후 재 크롤링 알고리즘 수정 필요 </ol>
</ol>
<ol> 오늘의 집 특성 상, 리뷰가 많이 달린 제품일 수록 상위에 노출하는 경향을 보여 하단 부는 데이터가 적어 의미가 없을 듯</ol>
<ol> 동작 환경 : Windows 8, Windows 10 </ol>

<H2> Result </H2>
<img src = "https://user-images.githubusercontent.com/43870121/101126668-50b7e280-363f-11eb-8640-c23cc718852a.png" width = "60%" height = "60%">
<img src = "https://user-images.githubusercontent.com/43870121/101126674-5281a600-363f-11eb-9502-d66e4a1c7c7f.png" width = "60%" height = "60%">

<hr>

<H1> 일간베스트 저장소 </H1>
<ol> 극단적 욕 데이터 수집을 위해 제작중 </ol>
<ol> 메인 페이지에서 목록 수집 후 긁어옴</ol>
<ol> 다음버튼 이벤트 호출 해야
  <ol> 일베는 버튼에 따로 클래스나 네임이 지정되있지 않아서 위치로 따야함</ol>
  <ol> 데이터 가져오는건 확인했는데 다음버튼 호출 + 마지막 버튼 이후 예외처리</ol>
</ol>
<ol> 커뮤니티 특성상 확실하게 욕으로 보이는 자연어를 많이 쓰고, 비유법이 적은걸 확인함</ol>
<ol> 동작 환경 : Ubuntu 16.04</ol>

<H1> 오늘의 유머 </H1>
<ol> 커뮤니티 특성상 비유적으로 상대를 욕하거나, 은어가 많음 </ol>

<hr>

<H1> 쿠팡 </H1>
<ol> 다이나믹 페이지로 리뷰탭 클릭 후, 스크립트를 호출해야 html 페이지 변경됨 </ol>
<ol> 검색한 키워드를 가진 품목은 전부 검색해 리뷰를 긁음 </ol>

<H1> Libs </H1>
<ol> Selenium </ol>
<ol> Chrome </ol>
<ol> Pandas </ol>
<ol> Soup4 </ol>
