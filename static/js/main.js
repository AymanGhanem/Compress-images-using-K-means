function getCompressedImageSizeBytes() {
    const base64String = document.getElementById("c-img").src;
    const stringLength = base64String.length - 'data:image/png;base64,'.length;
    const sizeInBytes = 4 * Math.ceil((stringLength / 3)) * 0.5624896334383812;
    return Math.ceil(sizeInBytes);
}
