/* DB 에 무조건 하나는 있어야 하는 데이터. */
insert into mainapp_influencer(name, profile_img_url) values('진경', 'https://elasticbeanstalk-ap-northeast-2-967883357924.s3.ap-northeast-2.amazonaws.com/influencer/hjk.jpeg');
update mainapp_influencer set id=1 where name='진경' and id != 1;