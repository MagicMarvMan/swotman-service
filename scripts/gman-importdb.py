import mysql.connector
import os

mydb = mysql.connector.connect(
  host=os.environ.get("DB_HOST"),
  user=os.environ.get("DB_USER"),
  passwd=os.environ.get("DB_PASSWD"),
  database=os.environ.get("DB_DATABASE")
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS `govdomains`;")
mycursor.execute("CREATE TABLE `govdomains` ( `id` INT NOT NULL AUTO_INCREMENT , `domain` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")

lines = [line.rstrip('\n') for line in open('final.txt', 'r')]
for line in lines:
    print(line)
    mycursor.execute("INSERT INTO `govdomains` (domain) VALUES ('" + line + "');")
    mydb.commit()
    print("Done with line.")
print("Done with importing.")


