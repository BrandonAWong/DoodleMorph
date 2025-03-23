type RGBA = [number, number, number, number];

const WIDTH = 1080;
const HEIGHT = 720;

// Get the color at a specific pixel
function getPixel(imageData: ImageData, x: number, y: number): RGBA {
  const index = (y * imageData.width + x) * 4;
  return [
    imageData.data[index], // Red
    imageData.data[index + 1], // Green
    imageData.data[index + 2], // Blue
    imageData.data[index + 3], // Alpha
  ];
}

// Compare two colors (RGBA arrays)
function colorsMatch(rgba1: RGBA, rgba2: RGBA): boolean {
  return (
    rgba1[0] === rgba2[0] && rgba1[1] === rgba2[1] && rgba1[2] === rgba2[2] && rgba1[3] === rgba2[3]
  );
}

// Set the color of a pixel
function setPixel(imageData: ImageData, x: number, y: number, rgba: RGBA): void {
  const index = (y * imageData.width + x) * 4;
  imageData.data[index] = rgba[0]; // Red
  imageData.data[index + 1] = rgba[1]; // Green
  imageData.data[index + 2] = rgba[2]; // Blue
  imageData.data[index + 3] = rgba[3]; // Alpha
}

// Convert hex color to RGBA array
export function hexToRGBA(hex: string): RGBA {
  const rgb = hex.match(/\w\w/g)?.map((x) => parseInt(x, 16)) || [0, 0, 0];
  return [...rgb, 255] as RGBA;
}

// Flood fill algorithm (4-way flood fill)
export function floodFill(
  ctx: CanvasRenderingContext2D,
  fillColor: RGBA,
  x: number,
  y: number,
): void {
  const imageData = ctx.getImageData(0, 0, WIDTH, HEIGHT);
  const startColor = getPixel(imageData, x, y);

  // If the target color is the same as fill color, exit
  if (colorsMatch(startColor, fillColor)) {
    return;
  }

  const pixelStack: [number, number][] = [[x, y]];

  while (pixelStack.length) {
    const [currentX, currentY] = pixelStack.pop() as [number, number];
    const currentColor = getPixel(imageData, currentX, currentY);

    if (colorsMatch(currentColor, startColor)) {
      setPixel(imageData, currentX, currentY, fillColor);

      // Push neighboring pixels onto the stack
      if (currentX > 0) pixelStack.push([currentX - 1, currentY]); // Left
      if (currentX < WIDTH - 1) pixelStack.push([currentX + 1, currentY]); // Right
      if (currentY > 0) pixelStack.push([currentX, currentY - 1]); // Up
      if (currentY < HEIGHT - 1) pixelStack.push([currentX, currentY + 1]); // Down
    }
  }

  ctx.putImageData(imageData, 0, 0);
}
