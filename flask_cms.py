from flask import Flask, render_template, request
import sqlite3 as sql
import csv, os
app = Flask(__name__)

@app.route('/')
def home():
   """This method displays home.html

   """
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   tcat = "tv_shows"
   tyear = "2023"
   cur = con.cursor()
   cur.execute("select * from dita where category1=? and text5=?", (tcat, tyear,))
   rows = cur.fetchall();

   tcat = "movies"
   tyear = "2023"
   cur = con.cursor()
   cur.execute("select * from dita where category1=? and text5=?", (tcat, tyear,))
   brows = cur.fetchall();


   tcat = "books"
   tyear = "2023"
   cur = con.cursor()
   cur.execute("select * from dita where category1=? and text5=?", (tcat, tyear,))
   crows = cur.fetchall();
   return render_template('home.html', rows = rows, brows = brows, crows = crows)
   
@app.route('/about/') 
def about(): 
    """This method displays about.html

    """
    return render_template('about.html') 

@app.route('/enternew')
def new_student():
   """This method displays new story form (form1.html).

   """
   with open('cat1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    crow = []
    for r in csv_reader:
        crow.append(r)
   return render_template('form1.html', crow = crow)
   
@app.route('/add_entry',methods = ['POST', 'GET'])
def new_entry():
   """This method displays new entry form (form2.html).

   """
   with open('cat1.csv') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       crow = []
       for r in csv_reader:
            crow.append(r)
   entry_id=request.args.get('id')
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from dita where id=?", (entry_id,))
   
   rows = cur.fetchall();
   return render_template('form2.html',rows = rows, crow = crow)
   
@app.route('/search1',methods = ['POST', 'GET'])
def search1():
   """This method displays a search form (form5.html).

   """
   with open('cat1.csv') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       crow = []
       for r in csv_reader:
            crow.append(r)
  
   return render_template('form5.html', crow = crow)

@app.route('/edit',methods = ['POST', 'GET'])
def edit():
   """This method displays edit entry form (form4.html).

   """
   with open('cat1.csv') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       crow = []
       for r in csv_reader:
            crow.append(r)
   entry_id=request.args.get('id')
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from dita where id=?", (entry_id,))
   
   rows = cur.fetchall();
   return render_template('form4.html',rows = rows, crow = crow)

@app.route('/edit1',methods = ['POST', 'GET'])
def edit1():
   """This method displays edit entry form (form3.html).

   """
   with open('cat1.csv') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       crow = []
       for r in csv_reader:
            crow.append(r)
   entry_id=request.args.get('id')
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from dita where id=?", (entry_id,))
   
   rows = cur.fetchall();
   return render_template('form3.html',rows = rows, crow = crow)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   """This method adds new story using data from story form (form1.html) and outputs result.html.

   """
   if request.method == 'POST':
      try:
         d_title = request.form['title']
         d_form_name = request.form['form_name']
         d_cat1 = request.form['category1']
         d_cat2 = request.form['category2']
         d_text1n = request.form['text1n']
         d_text2n = request.form['text2n']
         d_text3n = request.form['text3n']
         d_text4n = request.form['text4n']
         d_text5n = request.form['text5n']
         d_file1n = request.form['file1n']
         d_file2n = request.form['file2n']

         if not os.path.exists('static/' + d_form_name):
            os.mkdir('static/' + d_form_name)

         if not os.path.exists('static/' + d_form_name + "/images"):
            os.mkdir('static/' + d_form_name + "/images")

         with open("cat1.csv", "r") as f:
            cat1_list = f.read()
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO dita (title,form_name,category1,category2,text1n,text2n,text3n,text4n,text5n,file1n,file2n) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(d_title,d_form_name,d_cat1,d_cat2,d_text1n,d_text2n,d_text3n,d_text4n,d_text5n,d_file1n,d_file2n) )
            
            con.commit()
            msg = "Created directory: static/" + d_form_name + ". Record successfully added. Run 'sphinx-quickstart' on new directory."
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg, cat1_list = cat1_list)
         con.close()
		 
@app.route('/addrec2',methods = ['POST', 'GET'])
def addrec2():
   """This method adds new entry using data from entry form (form2.html) and outputs result.html.

   """
   if request.method == 'POST':
      try:
         d_title = request.form['title']
         d_form_name = request.form['form_name']
         d_short_desc = request.form['short_desc']
         d_cat1 = request.form['category1']
         d_cat2 = request.form['category2']
         d_text1 = request.form['text1']
         d_text1n = request.form['text1n']
         d_text2 = request.form['text2']
         d_text2n = request.form['text2n']
         d_text3 = request.form['text3']
         d_text3n = request.form['text3n']
         d_text4 = request.form['text4']
         d_text4n = request.form['text4n']
         d_text5 = request.form['text5']
         d_text5n = request.form['text5n']
         d_file1 = request.form['file1']
         d_file1n = request.form['file1n']
         d_file2 = request.form['file2']
         d_file2n = request.form['file2n']
         d_created_at = request.form['created_at']
         d_updated_at = request.form['updated_at']
         d_content = request.form['content']

         arr=[]
         arr=d_content.split("\n")
         f = open("static/" + d_cat1 + "/" + d_form_name + ".rst", "w+")
         for a in arr:
            f.write(a)
         f.close()
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO dita (title,form_name,short_desc,category1,category2,text1,text1n,text2,text2n,text3,text3n,text4,text4n,text5,text5n,file1,file1n,file2,file2n,created_at,updated_at,content) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(d_title,d_form_name,d_short_desc,d_cat1,d_cat2,d_text1,d_text1n,d_text2,d_text2n,d_text3,d_text3n,d_text4,d_text4n,d_text5,d_text5n,d_file1,d_file1n,d_file2,d_file2n,d_created_at,d_updated_at,d_content) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/editrec',methods = ['POST', 'GET'])
def editrec():
   """This method edits entry using data from entry form (form4.html) and outputs result.html.

   """
   if request.method == 'POST':
      try:
         d_title = request.form['title']
         d_form_name = request.form['form_name']
         d_short_desc = request.form['short_desc']
         d_cat1 = request.form['category1']
         d_cat2 = request.form['category2']
         d_text1 = request.form['text1']
         d_text2 = request.form['text2']
         d_text3 = request.form['text3']
         d_text4 = request.form['text4']
         d_text5 = request.form['text5']
         d_file1 = request.form['file1']
         d_file2 = request.form['file2']
         d_created_at = request.form['created_at']
         d_updated_at = request.form['updated_at']
         d_content = request.form['content']
         d_id = request.form['id']

         arr=[]
         arr=d_content.split("\n")
         f = open("static/" + d_cat1 + "/" + d_form_name + ".rst", "w+")
         for a in arr:
            f.write(a)
         f.close()
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
           
            cur.execute("UPDATE dita SET title=?,form_name=?,short_desc=?,category1=?,category2=?,text1=?,text2=?,text3=?,text4=?,text5=?,file1=?,file2=?,created_at=?,updated_at=?,content=? where id=?",(d_title,d_form_name,d_short_desc,d_cat1,d_cat2,d_text1,d_text2,d_text3,d_text4,d_text5,d_file1,d_file2,d_created_at,d_updated_at,d_content,d_id))
            con.commit()
            msg = "Record successfully updated"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/editrec1',methods = ['POST', 'GET'])
def editrec1():
   """This method edits entry using data from story form (form3.html) and outputs result.html.

   """
   if request.method == 'POST':
      try:
         d_title = request.form['title']
         d_form_name = request.form['form_name']
         d_cat1 = request.form['category1']
         d_cat2 = request.form['category2']
         d_text1n = request.form['text1n']
         d_text2n = request.form['text2n']
         d_text3n = request.form['text3n']
         d_text4n = request.form['text4n']
         d_text5n = request.form['text5n']
         d_file1n = request.form['file1n']
         d_file2n = request.form['file2n']
         d_id = request.form['id']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
           
            cur.execute("UPDATE dita SET title=?,form_name=?,category1=?,category2=?,text1n=?,text2n=?,text3n=?,text4n=?,text5n=?,file1n=?,file2n=? where id=?",(d_title,d_form_name,d_cat1,d_cat2,d_text1n,d_text2n,d_text3n,d_text4n,d_text5n,d_file1n,d_file2n,d_id))
            
            con.commit()
            msg = "Record successfully updated"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
         
@app.route('/searchlist',methods = ['POST', 'GET'])
def searchlist():
   """This method searches entries based on search string in search form (form5.html) and outputs result.html.

   """
   if request.method == 'POST':
      try:
         d_search1 = request.form['search1']
         d_cat1 = request.form['category1']
         
         
         with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            if d_cat1 == "all":
              cur.execute("select * from dita")
            else:
              cur.execute("select * from dita where category1=?", (d_cat1,))
            con.commit()
            rows = cur.fetchall();
            msg = "Search successfully executed all"
      except:
         con.rollback()
         msg = "error in insert operation" + d_cat1
      
      finally:
         return render_template("list1.html",msg = msg, rows = rows, d_search1 = d_search1)
         #return render_template("list.html",msg = msg, d_search1 = d_search1)
         con.close()
		 
@app.route('/delete', methods=['GET'])
def delete_entry():
   """This method deletes entry and outputs result.html.

   """
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   entry_id=request.args.get('id')
   cur.execute("delete from dita where id=?", (entry_id,))
   con.commit()
   rows = cur.fetchone();
   msg = "Record successfully deleted"
   return render_template("result.html",msg = msg)
    
@app.route('/list')
def list():
   """This method lists all entries.

   """
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from dita")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

@app.route('/list1', methods=['GET'])
def list1():
   """This method lists entries by category1.

   """
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   entry_cat1=request.args.get('category1')
   cur.execute("select * from dita where category1=?", (entry_cat1,))
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)


if __name__ == '__main__':
   #app.run(host = "192.168.1.19", debug = True)
   app.run(debug = True)

