

const blobToBase64 = (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = () => {
            resolve(reader.result.split(',')[1]);
        };
    });
};


export{
    blobToBase64
}

