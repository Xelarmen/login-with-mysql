# User Login-Register with MySql

## Install
Set Database and;

```
$ git clone https://github.com/Xelarmen/login-with-mysql
$ cd login-with-mysql
$ python usercontrol.py

```

## Database

Create new table. Its have 2 columns. 

Column Properties:
Type            = 'text'
Encoding Type   = 'utf8_general_ci'

## Rows that require personalization

#### Database Connection Information

4.Line

```
mydb = mysql.connector.connect(host="$$$",user="$$$",passwd="$$$",database="$$$",)

```
#### Table and Column Names

8.Line

```
kullanicisql = "SELECT COUNT(firstcolumnname) FROM `tablename` WHERE `firstcolumnname`='" + kadi + "'"

```
15.Line 

```
sql = "INSERT INTO `tablename`(`firstcolumnname`, `secondcolumnname`) VALUES ('" + kadi + "','" + sifre + "')"

```
25.Line

```
sql = "SELECT `secondcolumnname` FROM `tablename` WHERE `firstcolumnname`= '" + kadi + "' "

```
