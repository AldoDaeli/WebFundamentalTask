const rules = {
    username:{ min: 3,  msg: ["Username wajib diisi.", "Username minimal 3 karakter."] },
    password:{ min: 8,  msg: ["Password wajib diisi.", "Password minimal 8 karakter."] },
    nama:{msg: ["Nama wajib diisi."] },
    tgl_lahir:{ date: true, msg: ["Tanggal lahir wajib diisi.", "Tanggal lahir tidak boleh masa depan."] },
    alamat:{msg: ["Alamat wajib diisi."] },
    no_telpon: { prefix: "62", msg: ["Nomor telepon wajib diisi.", "Nomor telepon harus diawali 62."] },
};

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("registrasiForm").addEventListener("submit", (e) => {
    e.preventDefault();
    let valid = true;

    for (const [id, rule] of Object.entries(rules)) {
      const el  = document.getElementById(id);
      const err = document.getElementById("err-" + id);
      const val = el.value.trim();
      let msg   = "";

      if (!val) {
        msg = rule.msg[0];
      } else if (rule.min && val.length < rule.min) {
        msg = rule.msg[1];
      } else if (rule.date && new Date(val) > new Date()) {
        msg = rule.msg[1];
      } else if (rule.prefix && !val.startsWith(rule.prefix)) {
        msg = rule.msg[1];
      }

      err.textContent = msg;
      el.classList.toggle("border-red-500", !!msg);
      el.classList.toggle("border-gray-300", !msg);
      if (msg) valid = false;
    }

    if (valid) e.target.submit();
  });
});