# AWS Day5

### ELB
- 로드밸런싱이 필요한 이유와 역할 설명해보기  
  하나의 서버에 부하가 몰리지 않도록 여러대의 서버로 부하를 분산함으로서 서비스의 안정성, 가용성, 성능을 높이기 위해 사용합니다. 
- EC2 인스턴스 생성하기 (서울 리전, Bitnami Wordpress, t2.micro)
![](../../Images/AWS/AWS_Day_5/01_Instance1.png)
![](../../Images/AWS/AWS_Day_5/02_Instance2.png)
- ALB 생성하기 (EC2 인스턴스와 같은 리전)
![](../../Images/AWS/AWS_Day_5/03_ELB.png)
- 대상 그룹도 함께 생성하고 EC2 인스턴스를 대상 그룹에 포함시키기  
![](../../Images/AWS/AWS_Day_5/04_ELB.png)
- ALB의 주소를 통해 EC2 인스턴스에 접속하기
![](../../Images/AWS/AWS_Day_5/05_ELB_Address.png)
![](../../Images/AWS/AWS_Day_5/06_ELB_Address.png)
- EC2 인스턴스 종료하기
![](../../Images/AWS/AWS_Day_5/30_Deactivate_Instances.png)
![](../../Images/AWS/AWS_Day_5/26_Delete_ELB.png)
![](../../Images/AWS/AWS_Day_5/27_Delete_ELB_Group.png)

### Auto Scaling
- Auto Scaling이 필요한 이유와 역할 설명해보기  
  서버에 발생하는 부하에 능동적으로 대응하기 위한 방법으로 CPU사용율이나 네트워크 대역폭, 메모리 사용량 등이 설정치 이상으로 높아진다면 이미지화 되었는 가상의 서버를 구동하여 서비스 자원에 추가하고 서비스 이용율이 다시 낮아져 기준치 이하로 내려간다면 추가 생성되었던 서버를 서비스 자원에서 제외하여 불필요한 자원 낭비를 방지 합니다. 
- EC2 인스턴스 생성하기 (서울 리전, Bitnami Wordpress, t2.micro)
![](../../Images/AWS/AWS_Day_5/01_Instance1.png)
![](../../Images/AWS/AWS_Day_5/02_Instance2.png)
- 생성한 EC2 인스턴스를 기반으로 AMI 생성하기
![](../../Images/AWS/AWS_Day_5/07_AMI_Create.png)
- Auto Scaling Group(ASG) 만들기
![](../../Images/AWS/AWS_Day_5/10_Auto_Scaling.png)
- 시작 템플릿도 함께 생성하기
![](../../Images/AWS/AWS_Day_5/09_Auto_Scaling.png)
- ALB와 연결하기
![](../../Images/AWS/AWS_Day_5/11_AMI_Check.png)
- EC2 인스턴스에 ssh로 접속하고 stress를 사용하여 Auto Scaling 작동 테스트 하기
![](../../Images/AWS/AWS_Day_5/12_Ready_to_Stress.png)
![](../../Images/AWS/AWS_Day_5/13_Stress.png)
![](../../Images/AWS/AWS_Day_5/14_Create_New_Intance_by_Auto_Scaling.png)
- 모든 리소스(EC2, AMI, ASG, ALB 등) 정리하기
![](../../Images/AWS/AWS_Day_5/25_Delete_AS.png)
![](../../Images/AWS/AWS_Day_5/28_Deactivate_AMI.png)
![](../../Images/AWS/AWS_Day_5/29_Unregister_Deactivated_AMI.png)
![](../../Images/AWS/AWS_Day_5/30_Deactivate_Instances.png)

### RDS
- RDS 인스턴스 생성하기 (서울 리전, MySQL, db.t3.micro)
![](../../Images/AWS/AWS_Day_5/15_Create_RDS.png)
- MySQL Workbench를 사용하여 RDS 인스턴스에 접속하기
![](../../Images/AWS/AWS_Day_5/21_Connected_RDS.png)
![](../../Images/AWS/AWS_Day_5/22_Connected_RDS.png)
- RDS 인스턴스 삭제하기
![](../../Images/AWS/AWS_Day_5/23_Delete_RDS.png)


### S3
- S3 버킷 생성하기 (서울 리전)
![](../../Images/AWS/AWS_Day_5/16_Create_Bucket.png)
- 생성한 버킷에 파일 업로드 하기
![](../../Images/AWS/AWS_Day_5/17_Upload_to_Bucket.png)
- 업로드한 파일 다운로드 받기
![](../../Images/AWS/AWS_Day_5/18_Download_from_Bucket.png)
- 폴더를 생성하고 폴더로 파일 복제하기
![](../../Images/AWS/AWS_Day_5/19_Copy_to_Folder1.png)
![](../../Images/AWS/AWS_Day_5/20_Copied_to_Folder.png)
- 버킷 삭제하기
![](../../Images/AWS/AWS_Day_5/24_Delete_Bucket.png)