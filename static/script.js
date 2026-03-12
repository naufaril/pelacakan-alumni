function track(name){

fetch("/search",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({name:name})
})

.then(res=>res.json())
.then(data=>{

let html = `
<h3>${data.name}</h3>

<b>LinkedIn</b><br>
Perusahaan: ${data.linkedin.company}<br>
Jabatan: ${data.linkedin.position}<br>
Lokasi: ${data.linkedin.location}<br><br>

<b>Google Scholar</b><br>
Publikasi: ${data.scholar.publication}<br>
Institusi: ${data.scholar.institution}<br><br>

Status: ${data.status}
`

document.getElementById("result").innerHTML = html

})

}

function addAlumni(){

let data = {
nama: document.getElementById("nama").value,
program_studi: document.getElementById("prodi").value,
tahun_lulus: document.getElementById("tahun").value,
email: document.getElementById("email").value,
kota: document.getElementById("kota").value
}

fetch("/add_alumni",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify(data)
})
.then(res=>res.json())
.then(res=>{
alert(res.message)
location.reload()
})

}