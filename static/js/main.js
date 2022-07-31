function getCompressedImageSizeBytes() {
    const base64String = document.getElementById("c-img").src;
    const stringLength = base64String.length - 'data:image/png;base64,'.length;
    const sizeInBytes = 4 * Math.ceil((stringLength / 3)) * 0.5624896334383812;
    return Math.ceil(sizeInBytes);
}

function compressImage(e) {
    const colors = e.target.value;
    $("#selected-color").text(colors);

    const imageId = $("#o-img").data("image-id");

    const payload = {
        colors: colors,
    };
    $.post(compressUrl.replace("0", imageId), payload, function (data) {
        $("#c-img").attr("src", `data:image/png;base64,${data['image']}`);
        const size = getCompressedImageSizeBytes();
        $("#c-size").text(`${size}`);
    });
}
