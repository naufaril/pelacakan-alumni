// ================= LOAD DATA =================
async function loadAlumni(keyword = "") {
    try {
        const res = await fetch(`/get_alumni?keyword=${keyword}`);
        const data = await res.json();

        let html = "";

        if (data.length === 0) {
            html = `
            <tr>
                <td colspan="5" style="text-align:center;">Data tidak ditemukan</td>
            </tr>`;
        } else {
            data.forEach(a => {
                html += `
                <tr>
                    <td>${a.nama}</td>
                    <td>${a.tahun_lulus ?? "-"}</td>
                    <td>${a.program_studi}</td>
                    <td>${a.kota}</td>
                    <td>
                        <button onclick="searchTracer('${a.nama}')">🔍 Lacak</button>
                    </td>
                </tr>
                `;
            });
        }

        document.getElementById("alumniTable").innerHTML = html;

    } catch (error) {
        console.error("Error load data:", error);
    }
}

// ================= SEARCH =================
function searchAlumni() {
    const keyword = document.getElementById("searchInput").value;
    loadAlumni(keyword);
}

// ================= PELACAKAN + POPUP =================
async function searchTracer(name) {
    // tampilkan loading dulu
    document.getElementById("popupResult").innerHTML = `
        <p style="text-align:center;">⏳ Sedang melacak data...</p>
    `;
    document.getElementById("popup").style.display = "flex";

    try {
        const res = await fetch("/search", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name})
        });

        const data = await res.json();

        document.getElementById("popupResult").innerHTML = `
            <h3 class="popup-title">📊 Hasil Pelacakan</h3>

            <div class="popup-card">
                <p><b>👤 Nama:</b> ${data.name}</p>
                <p><b>🏢 Perusahaan:</b> ${data.linkedin.company}</p>
                <p><b>💼 Jabatan:</b> ${data.linkedin.position}</p>
                <p><b>📍 Lokasi:</b> ${data.linkedin.location}</p>
            </div>

            <div class="popup-card">
                <p><b>📚 Publikasi:</b> ${data.scholar.publication}</p>
                <p><b>🏫 Institusi:</b> ${data.scholar.institution}</p>
            </div>

            <div class="popup-card">
                <p><b>✅ Status:</b> ${data.status}</p>
            </div>
        `;

    } catch (error) {
        document.getElementById("popupResult").innerHTML = `
            <p style="color:red; text-align:center;">❌ Gagal mengambil data</p>
        `;
        console.error("Error search:", error);
    }
}

// ================= CLOSE POPUP =================
function closePopup() {
    document.getElementById("popup").style.display = "none";
}

// ================= CLOSE SAAT KLIK LUAR =================
window.onclick = function(event) {
    const popup = document.getElementById("popup");
    if (event.target === popup) {
        popup.style.display = "none";
    }
}

// ================= LOAD AWAL =================
window.onload = () => loadAlumni();
