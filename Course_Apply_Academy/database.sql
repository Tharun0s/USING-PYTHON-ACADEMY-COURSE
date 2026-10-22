CREATE DATABASE IF NOT EXISTS course_apply_academy;
USE course_apply_academy;

CREATE TABLE IF NOT EXISTS applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login_username VARCHAR(50) NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    qualification VARCHAR(100) NOT NULL,
    course_name VARCHAR(150) NOT NULL,
    course_fee DECIMAL(10,2) NOT NULL,
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: check saved applications
SELECT * FROM applications;
