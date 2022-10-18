function writeTextFile(afilename, output)
{
  var txtFile =new File(afilename);
  txtFile.writeln(output);
  txtFile.close();
}

var f="hello.txt"
writeTextFile(f,"je suis la .")

