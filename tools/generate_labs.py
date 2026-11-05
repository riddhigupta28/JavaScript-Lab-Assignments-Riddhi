from pathlib import Path
import subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1] / "javascript-lab-assignments"
# Original task implementations, following the topic list in each lab README.
LABS = [
("lab-1-first-javasript","First JavaScript Programs",[
("task1.html","Inline JavaScript updates a page message.",None,"<!doctype html><html><head><meta charset='utf-8'><title>First JavaScript</title></head><body><h1>My First JavaScript Page</h1><p id='message'>Loading...</p><script>const message='Hello, JavaScript!';document.getElementById('message').textContent=message;console.log(message);</script></body></html>","Hello, JavaScript!"),
("task2.js","Declare constants and variables.",'const college="Invertis University"; let semester=3; console.log(college); console.log("Semester:",semester); semester++; console.log("Next semester:",semester);',None,None),
("task3.js","Use a condition to select addition or subtraction.",'const a=18,b=7,operation="sum"; console.log("Result:",operation==="sum"?a+b:a-b);',None,None)]),
("lab-2-operators-calculator","Operators and Calculator",[
("task1.js","Perform arithmetic operations.",'const a=24,b=6; console.log("Add:",a+b); console.log("Subtract:",a-b); console.log("Multiply:",a*b); console.log("Divide:",a/b); console.log("Remainder:",a%b);',None,None),
("task2.js","Convert between strings and numbers.",'const value="42",number=Number(value); console.log(typeof value,value); console.log(typeof number,number); console.log("Concatenation:",value+8);',None,None),
("task3.js","Use a switch statement for a simple calculator.",'function calculate(a,op,b){switch(op){case "+":return a+b;case "-":return a-b;case "*":return a*b;case "/":return b? a/b:"Cannot divide by zero";default:return "Invalid operator";}} console.log(calculate(18,"+",6)); console.log(calculate(18,"*",6));',None,None)]),
("lab-3-conditions-loops","Conditions and Loops",[
("task1.js","Assign grades using if/else conditions.",'const marks=86; let grade;if(marks>=90)grade="A";else if(marks>=75)grade="B";else if(marks>=60)grade="C";else grade="Needs improvement";console.log("Grade:",grade);',None,None),
("task2.js","Print numbers 1 through 5 using a for loop.",'for(let n=1;n<=5;n++)console.log(n);',None,None),
("task3.js","Accumulate numbers in a while loop until total exceeds 20.",'let n=1,total=0;while(total<=20){total+=n;console.log(n,total);n++;}console.log("Final:",total);',None,None)]),
("lab-4-writing-functions","Writing Functions",[
("task1.js","Define and call a greeting function.",'function greet(name){return "Hello, "+name+"!";} console.log(greet("Riddhi Gupta"));',None,None),
("task2.js","Create an arrow function to return a square.",'const square=n=>n*n; console.log("Square:",square(9));',None,None),
("task3.js","Calculate a bill using a default tax rate.",'function bill(amount,tax=0.05){return amount*(1+tax);} console.log("Total:",bill(800)); console.log("With 8%:",bill(800,0.08));',None,None)]),
("lab-5-arrays-methods","Arrays and Array Methods",[
("task1.js","Read array length and first element.",'const subjects=["Java","JavaScript","Python","DBMS"];console.log(subjects.length,subjects[0]);',None,None),
("task2.js","Iterate through an array with forEach().",'["Java","JavaScript","Python"].forEach((s,i)=>console.log(i+1,s));',None,None),
("task3.js","Filter marks greater than or equal to 60.",'const marks=[45,72,88,39,61,95];console.log(marks.filter(x=>x>=60));',None,None),
("task4.js","Read an element from a two-dimensional array.",'const matrix=[[10,20],[30,40],[50,60]];console.log(matrix[1][0]);console.log(matrix[2]);',None,None)]),
("lab-6-json-text","JSON and Text",[
("task1.js","Serialize an object into JSON.",'const student={name:"Riya",roll:101,active:true};console.log(JSON.stringify(student));',None,None),
("task2.js","Parse JSON and print selected properties.",'const x=JSON.parse(\'{"course":"B.Tech CSE","semester":3}\');console.log(x.course,x.semester);',None,None),
("task3.js","Source task is empty in the supplied reference; no task statement was provided.","",None,"Source file empty. No output claimed.")]),
("lab-7-constructor-functions-classes","Constructor Functions and Classes",[
("task1.js","Create an object using a constructor function.",'function Student(name,roll){this.name=name;this.roll=roll;}const s=new Student("Aarav",204);console.log(s.name,s.roll);',None,None),
("task2.js","Define a Book class and print its summary.",'class Book{constructor(title,author){this.title=title;this.author=author;}summary(){return this.title+" by "+this.author;}}console.log(new Book("The Alchemist","Paulo Coelho").summary());',None,None),
("task3.js","Add a result() method through a constructor prototype.",'function Candidate(name,marks){this.name=name;this.marks=marks;}Candidate.prototype.result=function(){return this.marks>=40?"Pass":"Fail";};console.log(new Candidate("Neha",78).result());',None,None)]),
("lab-8-inheritance-methods-composition","Inheritance, Methods and Composition",[
("task1.js","Extend Person with Teacher and use an inherited method.",'class Person{constructor(name){this.name=name;}introduce(){return "My name is "+this.name;}}class Teacher extends Person{teach(){return this.name+" teaches JavaScript";}}const t=new Teacher("Meera");console.log(t.introduce(),t.teach());',None,None),
("task2.js","Check PIN values using a class method.",'class Security{constructor(pin){this.pin=String(pin);}check(value){return this.pin===String(value);}}const s=new Security(2468);console.log(s.check(2468),s.check(1234));',None,None),
("task3.js","Compose a Car from an Engine object.",'const engine={start(){return "Engine started";}};class Car{constructor(model,unit){this.model=model;this.engine=unit;}start(){return this.model+": "+this.engine.start();}}console.log(new Car("City",engine).start());',None,None)]),
("lab-9-dom-validation-storage-quiz","DOM, Form Validation, Local Storage and Quiz",[
("task1.html","Change a heading when a button is clicked.",None,"<!doctype html><html><head><meta charset='utf-8'><title>DOM Practice</title></head><body><h1 id='heading'>Welcome to JavaScript</h1><button id='change'>Change text</button><script>document.getElementById('change').addEventListener('click',()=>document.getElementById('heading').textContent='Text changed successfully!');</script></body></html>","Browser preview: heading changes after clicking the button."),
("task2.js","Validate a name and return an error list.",'function validateName(name){const errors=[];if(!name.trim())errors.push("Name is required");if(name.trim().length===1)errors.push("Name is too short");return errors;}console.log(validateName("Riddhi Gupta"));console.log(validateName(""));',None,None),
("task3.html","Save a note in localStorage and show it after reload.",None,"<!doctype html><html><head><meta charset='utf-8'><title>Quick Notes</title></head><body><h1>Quick Notes</h1><input id='note' aria-label='Your note'><button id='save'>Save note</button><p id='saved'></p><script>const n=document.getElementById('note'),p=document.getElementById('saved');n.value=localStorage.getItem('lab-note')||'';p.textContent=n.value?'Saved note: '+n.value:'No saved note yet';document.getElementById('save').addEventListener('click',()=>{localStorage.setItem('lab-note',n.value);p.textContent='Saved note: '+n.value;});</script></body></html>","Browser preview: Quick Notes uses localStorage; test through localhost."),
("task4.html","Select a quiz answer and display whether it is correct.",None,"<!doctype html><html><head><meta charset='utf-8'><title>Mini Quiz</title></head><body><h1>Mini Quiz</h1><p>What is 2 + 3?</p><button data-answer='4'>4</button><button data-answer='5'>5</button><button data-answer='6'>6</button><p id='result'></p><script>document.querySelectorAll('button[data-answer]').forEach(b=>b.addEventListener('click',()=>document.getElementById('result').textContent=b.dataset.answer==='5'?'Correct!':'Try again'));</script></body></html>","Browser preview: quiz answer 5 displays Correct!")]),
("lab-10-objects-destructuring","Objects and Destructuring",[
("task1.js","Read and update a property on an object.",'const student={name:"Isha",semester:2};console.log(student.semester);student.semester=3;console.log(student.semester);',None,None),
("task2.js","Extract array elements with array destructuring.",'const colors=["Blue","Green","Orange"];const [first,second]=colors;console.log(first,second);',None,None),
("task3.js","Extract object properties with object destructuring.",'const profile={name:"Kabir",course:"B.Tech CSE"};const {name,course}=profile;console.log(name,course);',None,None)]),
("lab-11-scope-closures","Scope and Closures",[
("task1.js","Demonstrate block scope.",'const message="outside";if(true){const local="inside block";console.log(local);}console.log(message);',None,None),
("task2.js","Create a counter whose closure retains its count.",'function createCounter(){let count=0;return ()=>++count;}const counter=createCounter();console.log(counter(),counter(),counter());',None,None),
("task3.js","Read a global variable from inside a function.",'const college="Invertis University";function showCollege(){console.log(college);}showCollege();',None,None)]),
("lab-12-callbacks-higher-order-functions","Callbacks and Higher-Order Functions",[
("task1.js","Pass a callback to a function and apply it twice.",'function applyTwice(value,fn){return fn(fn(value));}console.log(applyTwice(5,n=>n*2));',None,None),
("task2.js","Format marks using a callback.",'function displayMarks(marks,formatter){marks.forEach(x=>console.log(formatter(x)));}displayMarks([62,75,91],x=>"Marks: "+x);',None,None),
("task3.js","Run a callback three times with a round number.",'function repeat(fn){for(let i=1;i<=3;i++)fn(i);}repeat(i=>console.log("Round",i));',None,None)]),
("lab-13-reduce-some-every-map","reduce(), some(), every() and map()",[
("task1.js","Calculate the sum of prices using reduce().",'const prices=[120,250,80,150];console.log(prices.reduce((sum,x)=>sum+x,0));',None,None),
("task2.js","Check some marks below 40 and all marks at least 35.",'const marks=[42,55,38,71];console.log(marks.some(x=>x<40));console.log(marks.every(x=>x>=35));',None,None),
("task3.js","Create an updated marks array using map().",'const marks=[50,65,70];const updated=marks.map(x=>x+5);console.log(marks);console.log(updated);',None,None)]),
("lab-14-timers-intervals","Timers and Intervals",[
("task1.js","Show synchronous output around a zero-delay timeout.",'console.log("First");setTimeout(()=>console.log("Timeout callback"),0);console.log("Second");',None,None),
("task2.js","Cancel a scheduled timeout before it runs.",'const timer=setTimeout(()=>console.log("Should not print"),100);clearTimeout(timer);console.log("Timeout cancelled");',None,None),
("task3.js","Print three interval ticks and stop the interval.",'let ticks=0;const timer=setInterval(()=>{console.log("Tick",++ticks);if(ticks===3)clearInterval(timer);},100);',None,None)]),
("lab-15-promises-async-await","Promises and Async/Await",[
("task1.js","Resolve a Promise for a valid marks value.",'function checkMarks(m){return new Promise(resolve=>{if(m>=0&&m<=100)resolve("Valid marks: "+m);});}checkMarks(82).then(console.log);',None,None),
("task2.js","Reject an out-of-range marks value and handle the error.",'function checkMarks(m){return new Promise((resolve,reject)=>m>=0&&m<=100?resolve("Valid marks"):reject(new Error("Marks must be between 0 and 100")));}checkMarks(125).catch(e=>console.log("Error:",e.message));',None,None),
("task3.js","Source task is empty in the supplied reference; no task statement was provided.","",None,"Source file empty. No output claimed."),
("task4.js","Resolve a simulated user list and print each name with async/await.",'async function showUsers(){const users=await Promise.resolve([{name:"Aarav"},{name:"Riya"},{name:"Kabir"}]);users.forEach(u=>console.log(u.name));}showUsers();',None,None)])
]

def make_font(size,bold=False):
    choices=["/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"]
    for p in choices:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

def render_png(path,title,task,output):
    lines=[]
    for line in (output or "No console output").splitlines():
        lines += textwrap.wrap(line,width=88) or [""]
    lines=lines[:12]
    h=max(240,140+30*len(lines))
    im=Image.new("RGB",(1100,h),(28,31,36)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((12,12,1088,h-12),radius=14,fill=(36,40,47),outline=(75,83,96),width=2)
    for x,c in [(30,(255,95,86)),(54,(255,190,60)),(78,(40,200,90))]: d.ellipse((x,28,x+14,42),fill=c)
    d.text((118,24),"JavaScript Lab | Output Preview",font=make_font(19,True),fill=(205,215,228))
    d.line((25,65,1075,65),fill=(80,89,102),width=2)
    d.text((30,82),title[:90],font=make_font(14,True),fill=(122,190,255))
    d.text((30,106),task[:95],font=make_font(12),fill=(190,200,212))
    y=140
    for line in lines: d.text((32,y),line[:100],font=make_font(16),fill=(239,242,246)); y+=28
    im.save(path,format="PNG",optimize=True)

ROOT.mkdir(parents=True,exist_ok=True)
total=0
for slug,title,tasks in LABS:
    folder=ROOT/slug; folder.mkdir(parents=True,exist_ok=True)
    readme=[f"# {title}","","Student: Riddhi Gupta  ","University Roll Number: BCS2025468  ","Invertis University, Bareilly","","## Tasks and Results",""]
    for i,(filename,desc,code,html,preview) in enumerate(tasks,1):
        path=folder/filename
        if filename.endswith(".html"):
            path.write_text(html,encoding="utf-8")
            output=preview or "Open in a browser to test the page."
            result="HTML preview panel created; test page interactions in a browser."
        else:
            path.write_text(code or "",encoding="utf-8")
            if code:
                run=subprocess.run(["node",str(path)],capture_output=True,text=True,timeout=12)
                if run.returncode: raise RuntimeError(f"{path}: {run.stderr}")
                output=preview or run.stdout.strip() or "Program completed."
                result="JavaScript syntax checked and executed with Node.js."
            else:
                output=preview or "Source file empty; no output claimed."
                result="Not executed: source task is empty in supplied reference."
        image=folder/(Path(filename).stem+"-output.png")
        render_png(image,title,f"Task {i}: {desc}",output)
        readme += [f"### Task {i} — {filename}","",desc,"",f"Evidence: {image.name}",f"Result: {result}",""]
        total+=1
    readme += ["## How to Run","","Run JavaScript with Node.js from this folder, for example: node task1.js.","Open HTML files in a modern browser and use the page controls.","","## Evidence Note","","PNG files are generated output-preview panels, not live screenshots of an IDE or browser. Verify interactive HTML behaviour in a browser before submission.",""]
    (folder/"README.md").write_text("\n".join(readme),encoding="utf-8")
print(f"Generated {len(LABS)} labs and {total} output-preview images.")

# Regeneration trigger: build the generated lab portfolio on the next workflow run.
