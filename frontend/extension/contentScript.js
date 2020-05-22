console.log("Get Caged: Loaded!")

// Updated url before publishing
const backendUrl = "http://localhost:8000"
let imgs = document.querySelectorAll("img")

function getRandomElements(list, n = Math.floor(Math.random() * list.length) ){
    tmpList = [...list]
    return Array(n).fill().map( 
        _ => tmpList.splice(Math.floor(Math.random() * tmpList.length), 1)[0]
    )
}

console.log(imgs, document)


if( imgs?.length > 0 ){
    let firstImg = imgs[0]
    
    console.log(
        "First Image:", 
        {src: firstImg.src, height: firstImg.height, width: firstImg.width},
    )

    let randImgs = getRandomElements(imgs)
    // console.log(randImgs)

    for (let img of randImgs){
        // console.log(img)
        // img.src = "https://images.askmen.com/1080x540/2016/11/11-084440-nicolas_cage_life_lessons.jpg"
        const {width, height} = img
        img.src = `${backendUrl}/cage?width=${width}&height=${height}`
    }

} else {
    console.log("No images found on page")
}
