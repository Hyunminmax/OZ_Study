# 스래싱, 워킹셋
## 스래싱  
컴퓨터 시스템에서 메모리 사용량이 너무 많거나 메모리가 부족하여 페이지 폴드(프로세스가 요구하는 데이터가 메모리가 아닌 디스크에 있는 경우)가 빈번하게 발생하여 시스템의 성능이 급격하게 저하되는 현상
## 위킹셋
스래싱을 소프트웨어 적인 방법으로 해결하기 위해 만들어진 방법.
프로세스가 실제로 참조하는 메모리 페이지의 집합을 워킹셋으로 하고 각 워킹셋에 필요한 최소한의 메모리를 할당한다. 
주기적으로 워킹셋의 페이지들이 활성화되어 필요한지를 검사하고 가장 오랜시간 사용되지 않은 페이지는 워킹셋 공간에서 제거해 워킹셋에는 자주 사용되며 지금 빈번하게 사용되는 페이지들만이 남고 여유 공간에 새로운 페이지를 로딩하여 페이지 폴드를 최소화 한다. 