/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - university project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`university project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `university project`;

/*Table structure for table `allocate` */

DROP TABLE IF EXISTS `allocate`;

CREATE TABLE `allocate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `allocate` */

/*Table structure for table `assignwork` */

DROP TABLE IF EXISTS `assignwork`;

CREATE TABLE `assignwork` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `p_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `assignwork` */

insert  into `assignwork`(`a_id`,`teacher_id`,`p_id`,`date`,`status`) values 
(1,7,1,'2022-08-31','assigned'),
(2,7,2,'2022-09-02','assigned'),
(3,7,3,'2022-09-02','assigned'),
(4,7,3,'2022-09-02','assigned');

/*Table structure for table `college` */

DROP TABLE IF EXISTS `college`;

CREATE TABLE `college` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_lid` int(11) DEFAULT NULL,
  `college_name` varchar(50) DEFAULT NULL,
  `established_year` varchar(50) DEFAULT NULL,
  `college_email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `college` */

insert  into `college`(`c_id`,`c_lid`,`college_name`,`established_year`,`college_email`,`phone`,`place`,`post`,`pin`) values 
(3,4,'nesra','1983','nesra@gmail.com',89645738,'thirurkkad','angadippuram',679369),
(8,19,'polytechnic','1948','poly@1gmail.com',9446289847,'wayanad','kkk',670645);

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_id` int(11) DEFAULT NULL,
  `course` varchar(50) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `fees` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`dept_id`,`course`,`duration`,`fees`) values 
(1,1,'bca','3year','12000'),
(2,5,'bba',NULL,NULL),
(3,6,'biology','1','1000'),
(6,3,'admin','2','23456789'),
(7,3,'bsc','3year','100000'),
(8,3,'bcom','3year','100000'),
(9,3,'bca','3year','100000'),
(12,3,'university','4year','100');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `d_id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`d_id`,`department`) values 
(3,'science'),
(4,'physics'),
(6,'biology'),
(8,'mca'),
(9,'BA');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`lid`,`feedback`,`date`) values 
(1,7,'feedb','2021-08-08'),
(2,8,'gfgcfg','2021-08-08'),
(3,8,'bsddd','2022-09-10'),
(4,8,'Sidharth Sidhu','2022-09-10'),
(5,8,'j clin DD pu ga','2022-09-11');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','Admin@12','university'),
(2,'sndpyss','Sndp@123','college'),
(3,'gems','gem','college'),
(4,'nesra','nes','college'),
(6,'feroke','fer','college'),
(7,'t','t','teacher'),
(8,'tyd','tyd','student'),
(9,'arsh','arshaaa','teacher'),
(10,'prem','sidharth','teacher'),
(11,'dfghjkl','fghjk','teacher'),
(12,'fghjk','rtyuik','teacher'),
(15,'sidhu','sidhu@123','teacher'),
(16,'prem','sidhu@123','teacher'),
(17,'ais','Aisw@rya888','teacher'),
(18,'ais','Aisw@rya88','teacher'),
(19,'aishu','Aish@123','college'),
(20,'nayan','Nayana@123','teacher'),
(26,'sidhu','kannappi','student');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `sem` varchar(50) DEFAULT NULL,
  `notification` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`n_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`n_id`,`course_id`,`sem`,`notification`,`date`) values 
(1,1,'1','fghjm','2022-08-27'),
(2,1,'1','bgfsdfghjkl','2022-08-27'),
(3,2,'2','mjhgkjbg','2022-08-27'),
(4,1,'4','yjdfjy','2022-08-29'),
(6,1,'4','uyf','2022-08-29'),
(8,1,'1','rtetqtwyuetyi','2022-09-03');

/*Table structure for table `project` */

DROP TABLE IF EXISTS `project`;

CREATE TABLE `project` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_id` int(11) DEFAULT NULL,
  `topic` varchar(50) DEFAULT NULL,
  `abstract` text,
  `area` varchar(50) DEFAULT NULL,
  `description` text,
  `status` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `project` */

insert  into `project`(`p_id`,`s_id`,`topic`,`abstract`,`area`,`description`,`status`,`date`) values 
(13,8,'test1','static/abstract/20220911-121149','test 1',NULL,'pending','2022-09-11'),
(14,8,'test2','static/abstract/20220911-121842.jpg','test2',NULL,'pending','2022-09-11'),
(15,8,'ghfhg','static/abstract/20220911-122107.jpg','',NULL,'pending','2022-09-11'),
(16,8,'hhhd','static/abstract/20220911-142251.jpg','vvgg','Crimes are a common social problem affecting the quality of life and the economic growth of a society. It is considered an essential factor that determines whether or not people move to a new city and what places should be avoided when they travel. With the increase of crimes, law enforcement agencies are continui','accepted','2022-09-11');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `genter` varchar(50) DEFAULT NULL,
  `college_id` int(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`s_id`,`l_id`,`course_id`,`firstname`,`lastname`,`dob`,`genter`,`college_id`,`email`,`contact`,`place`,`post`,`pin`,`dept_id`) values 
(1,8,3,'sidhu','s','2021-01-18','male',NULL,'uj',NULL,NULL,NULL,NULL,NULL),
(2,2,3,'favas','fdsf','2022-09-10','female',NULL,'yhgnb',NULL,NULL,NULL,NULL,NULL),
(3,10,3,'arsha','mp','2022-09-05','male',NULL,'sdcf',NULL,NULL,NULL,NULL,NULL),
(5,9,3,'aish','warya','2022-02-01',NULL,NULL,'edfg',NULL,NULL,NULL,NULL,NULL),
(10,27,0,'sidhu','kannappi','01-04-2000','Female',0,'sidhukannappi@gmail.com',9547863217,'poonjikara','poonjikara ',676593,0),
(16,33,1,'','','','Female',4,'',0,'','',0,3),
(17,34,1,'','','','Female',4,'',0,'','',0,3);

/*Table structure for table `teachers` */

DROP TABLE IF EXISTS `teachers`;

CREATE TABLE `teachers` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) DEFAULT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `department_id` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `teachers` */

insert  into `teachers`(`teacher_id`,`college_id`,`firstname`,`lastname`,`gender`,`department_id`,`pin`,`lid`,`place`,`post`,`phone`,`email`) values 
(1,NULL,'favs','vg',NULL,NULL,NULL,7,NULL,NULL,NULL,NULL),
(7,2,'favas','kannan','male','SELECT',123456,15,'asdfgg','aszxdfg',6543212345,'sidharthsidhu708@gmail.com'),
(10,2,'aiswarya','krishna','female','SELECT',670644,18,'mananthavady','thavinhal',9446289847,'a@gmail.com'),
(11,2,'nayana','banu','female','4',456789,20,'valamboor','anga',9876543212,'nayanabanu123@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
