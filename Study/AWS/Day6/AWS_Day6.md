# AWS Day6  

### S3(정적 웹사이트 호스팅)
- S3 버킷 생성하기 (서울 리전)
![alt text](../../Images/AWS/Day_6/01_Create_Bucket.png)
- 버킷의 정적 웹사이트 호스팅 활성화 하기
![alt text](../../Images/AWS/Day_6/02_Activate_Static_Bucket.png) 
- 생성한 버킷에 간단하게 작성한 index.html 파일 업로드 하기
![alt text](../../Images/AWS/Day_6/03_Upload_index_to_Bucket.png) 
- 버킷의 퍼블릭 액세스 차단 해제하기
![alt text](../../Images/AWS/Day_6/04_Change_Policy_Bucket.png) 
- 버킷 정책 편집하기 (외부에서 모든 객체에 접근할 수 있도록)
![alt text](../../Images/AWS/Day_6/05_Change_Policy_Bucket.png) 
- 버킷 웹 사이트 엔드포인트로 접속하여 웹 사이트가 잘 나오는지 확인하기
![alt text](../../Images/AWS/Day_6/06_Change_Policy_Bucket.png) 
- 버킷 삭제하기  
![alt text](../../Images/AWS/Day_6/19_Delete_Bucket.png) 


### CloudFront  

- S3 버킷 생성하기 (서울 리전)
![alt text](../../Images/AWS/Day_6/01_Create_Bucket.png)
- 생성한 버킷을 origin으로 하는 CloudFront 배포 생성하기 (원본 액세스 제어 설정 포함)
![alt text](../../Images/AWS/Day_6/08_CloudFront_Publish.png) 
- 배포 생성 후 S3 버킷 정책 업데이트 하기 (CloudFront가 버킷의 모든 객체에 접근할 수 있도록)
![alt text](../../Images/AWS/Day_6/07_Change_Policy_Bucket.png) 
- CloudFront 배포 도메인 이름으로 접속하여 객체가 잘 나오는지 확인하기
![alt text](../../Images/AWS/Day_6/09_CloudFront_Publish.png) 
- CloudFront 배포 및 S3 버킷 삭제하기  
![alt text](../../Images/AWS/Day_6/20_Delete_CloudFront.png)
![alt text](../../Images/AWS/Day_6/19_Delete_Bucket.png) 


### Route 53  
- 호스팅 영역 생성하기  
![alt text](../../Images/AWS/Day_6/10_Create_HostingArea_Route53.png) 
- A 레코드 추가하기
![alt text](../../Images/AWS/Day_6/11_A_Record_on_Route53.png) 
- CNAME 레코드 추가하기
![alt text](../../Images/AWS/Day_6/12_Cname_Record_on_Route53.png) 
- NS, SOA 레코드를 제외한 모든 레코드 삭제하기  
![alt text](../../Images/AWS/Day_6/13_Delete_Records_Route53.png) 
- 호스팅 영역 삭제하기  
![alt text](../../Images/AWS/Day_6/18_Delete_HostingArea_Route53.png) 

### IAM  

- IAM 사용자 생성하기 (Management Console 액세스, EC2ReadOnlyAccess 권한 포함)
![alt text](../../Images/AWS/Day_6/14_Create_User_IAM.png) 
- 생성한 IAM 사용자로 AWS 콘솔 로그인하기
![alt text](../../Images/AWS/Day_6/15_Login_IAM.png) 
- EC2 페이지 접속해서 잘 나오는지 확인하기
![alt text](../../Images/AWS/Day_6/16_Check_Login_IAM.png) 
- IAM 사용자 삭제하기  
![alt text](../../Images/AWS/Day_6/17_Delete_User_IAM.png) 