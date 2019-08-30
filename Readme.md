# User Login-Register with MySql

## Install
Set Database and;

```
$ git clone https://github.com/Xelarmen/login-with-mysql
$ cd usercontrol
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

14.Line

```
kullanicisql= "SELECT COUNT(firstcolumnname) FROM `tablename` WHERE `firstcolumnname`='"+kullanici+"'"

```
20.Line 

```
sql = "INSERT INTO `tablename`(`firstcolumnname`, `sifre`) VALUES ('"+kullanici +"','"+sifre+"')"

```
35.Line

```
sql ="SELECT `secondcolumnname` FROM `tablename` WHERE `firstcolumnname`= '"+kullanici+"' "

```