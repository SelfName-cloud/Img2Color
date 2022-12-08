import React from "react";
import { useEffect, useState } from "react";
import { Button } from 'react-bootstrap';
import axios from "axios";
  


function TestIt ( ) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isFilePicked, setIsFilePicked] = useState(false);

  const changeHandler = (event) => {
      setSelectedFile(event.target.files[0]);
      setIsFilePicked(true);
  };
  
  const handleSubmit = event => {
    event.preventDefault();
    const formData2 = new FormData();
    formData2.append(
      "file",
      selectedFile,
      selectedFile.name
    );
    
  const requestOptions = {
      method: 'POST',
      headers: { },  
      //mode: 'no-cors',
      body: formData2
  };
    fetch('http://127.0.0.1:8000/upload', requestOptions)
      .then(response => response.json()) //response.json()
      .then(function (response) {
        console.log('response')
        console.log(response)
          });
  }
  return (  <div>
      <form onSubmit={handleSubmit}>
        <fieldset>
            <input name="image" type="file" onChange={changeHandler} accept=".jpeg, .png, .jpg"/>
        </fieldset>
        <Button type="submit">Save</Button>
      </form>
  </div>
);
}
export default TestIt;