const express = require("express");
const { exec } = require("child_process");
const app = express();

app.use(express.static(__dirname));

app.get("/scan",(req,res)=> {
  exec("arp-scan --localnet",(err,stdout)=> {
    if (err)
      return res.json([]);
  }

  const device = stdout
  .split("\n")
  .filter(l => l.match(/([0-9a-f]{2}:){5}/i))
  .map(l=> {

      const p = l.split(/\s+/);
      return {
        ip: p[0];
        mac: p[1];
        vendor: p.slice(2).join("")
      };
    });

    res.json(device);
  });
});

app.listen(3000,()=> {
  console.log("Starting Server at http://localhost:3000");
});
