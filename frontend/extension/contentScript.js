console.log("Get Caged: Loaded!")

// Updated url before publishing
const backendUrl = "http://localhost:8000"
let imgs = document.querySelectorAll("img")

function getRandomElements(list, n = constrainedRandom(list.length) ){
    tmpList = [...list]
    return Array(n).fill().map( 
        _ => tmpList.splice(Math.floor(Math.random() * tmpList.length), 1)[0]
    )
}

function constrainedRandom(maxNum, minNum = 3) {
    const minSafeNum = Math.min(Math.max(minNum, maxNum * 0.03), maxNum)
    return Math.floor(Math.random()*(maxNum-minSafeNum+1)+minSafeNum);
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
        if ((width >= 12) && (height >= 12)) {
            img.src = `${backendUrl}/cage?width=${width}&height=${height}`
        } else {
            console.log("Image is too small, won't fetch cage image")
        }
    }

} else {
    console.log("No images found on page")
}
