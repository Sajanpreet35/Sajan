let video = document.getElementById("camera");
async function startCamera() {
    try {
        let stream = await navigator.mediaDevices.getUserMedia({video:true,audio:false});
        video.srcObject = stream;
    } catch(err) { alert("Camera not accessible: "+err); }
}
startCamera();

async function askAI(){
    let question = document.getElementById("question").value;
    if(!question) return alert("Type a question!");
    try{
        let res = await fetch("http://localhost:8000/ask", {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({question})
        });
        let data = await res.json();
        document.getElementById("response").innerText = data.answer;
    }catch(err){
        document.getElementById("response").innerText="Error: "+err;
    }
}
