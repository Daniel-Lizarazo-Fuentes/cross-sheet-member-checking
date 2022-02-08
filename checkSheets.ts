import XLSX from "https://deno.land/x/sheetjs@v0.17.5/dist/xlsx.js";

const file = XLSX.readFile('test.xlsx');


console.log(file)