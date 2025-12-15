#!/usr/bin/env -S bun run
const inputs = await Bun.file("input.txt").text()

function maxdex(arr) {
  return arr.reduce((acc, val, idx) => {
    let [elem, maxidx] = acc
    if (val > elem) {
      elem = val
      maxidx = idx
    }
    return [elem, maxidx]
  }, [arr[0], 0])
}

function joltage(bank, limit) {
  const result = []
  let offset = 0
  let n = bank.length
  for (let stop = limit - 1; stop >= 0; --stop) {
    const slc = bank.slice(offset, n - stop)
    const [elem, idx] = maxdex(Array.from(slc))
    offset = offset + idx + 1
    result.push(elem)
  }
  return Number(result.join``)
}

console.log(
  inputs
    .split`\n`
    .map(n => [joltage(n, 2), joltage(n, 12)])
    .reduce((a, b) => [a[0] + b[0], a[1] + b[1]])
    .join`\n`
)
