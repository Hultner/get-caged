console.log("Get Caged: Loaded!")

let imgs = document.querySelectorAll("img")

console.log(imgs, document)


if( imgs?.length > 0 ){
    let firstImg = imgs[0]
    
    console.log(
        "First Image:", 
        {src: firstImg.src, height: firstImg.height, width: firstImg.width},
    )

} else {
    console.log("No images found on page")
}
