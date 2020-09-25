from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/prod")
def prod():
	return render_template('prod.html')

@app.route("/locate")
def locate():
	return render_template('locate.html')

@app.route("/prodMove")
def prodMove():
	return render_template('prodMove.html')

@app.route("/addProd")
def addProd():
	return render_template('addProd.html')

@app.route("/editProd")
def editProd():
	con=sqlite3.connect("details.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("Select * from Product")
	rows=cur.fetchall()
	return render_template('editProd.html',rows=rows)

@app.route("/viewProd")
def viewProd():
	con=sqlite3.connect("details.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("Select * from Product")
	rows=cur.fetchall()
	return render_template('viewProd.html',rows=rows)

@app.route("/saveProd",methods=["POST","GET"])
def saveProd():
	if request.method=='POST':
		try:
			Prod_id=request.form["Prod_id"]
			with sqlite3.connect("details.db") as con:
				cur=con.cursor()
				cur.execute("Insert into Product(Prod_id)values(Prod_id)")
				con.commit()
				msg="Added Successfully"
		except:
			con.rollback()
			msg="Error"
		finally:
			return render_template('result.html',msg=msg)
			con.close()
	else:
		return render_template('prod.html')


@app.route("/addLoc")
def addLoc():
	return render_template('addLoc.html')

@app.route("/editLoc")
def editLoc():
	return render_template('editLoc.html')

@app.route("/viewLoc")
def viewLoc():
	con=sqlite3.connect("details.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("Select * from Location")
	rows=cur.fetchall()
	return render_template('viewLoc.html',rows=rows)

@app.route("/saveLoc",methods=["POST","GET"])
def saveLoc():
	if request.method=='POST':
		try:
			loc_id=request.form["loc_id"]
			with sqlite3.connect("details.db") as con:
				cur=con.cursor()
				cur.execute("Insert into Location(Location_id)values(loc_id)")
				con.commit()
				msg="Added Successfully"
		except:
			con.rollback()
			msg="Error"
		finally:
			return render_template("result.html",msg=msg)
			con.close()

@app.route("/addMove")
def addMove():
	return render_template('addMove.html')

@app.route("/editMove")
def editMove():
	return render_template('editMove.html')

@app.route("/viewMove")
def viewMove():
	con=sqlite3.connect("details.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("Select * from ProdMove")
	rows=cur.fetchall()
	return render_template('viewMove.html',rows=rows)

@app.route("/saveMove",methods=["POST","GET"])
def saveMove():
	if request.method=='POST':
		try:
			move_id=request.form["move_id"]
			from_loc=request.form["from_loc"]
			to_loc=request.form["to_loc"]
			p_id=request.form["p_id"]
			qty=request.form["qty"]
			with sqlite3.connect("details.db") as con:
				cur=con.cursor()
				cur.execute("Insert into ProdMove(move_id,Timestamp,from_location,to_location,Prod_id,Qty) values(move_id,from_loc,to_loc,p_id,qty)")
				con.commit()
				msg="Added Successfully"
		except:
			con.rollback()
			msg="Error"
		finally:
			return render_template("result.html",msg=msg)
			con.close()

@app.route("/report")
def report():
	con=sqlite3.connect("details.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("Select Prod_id,from_location,to_location,Qty from ProdMove")
	rows=cur.fetchall()
	return render_template('report.html',rows=rows)

if __name__=="__main__":
	app.run(debug=True)