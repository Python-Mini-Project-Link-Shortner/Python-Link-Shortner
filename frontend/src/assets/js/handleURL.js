// URL 파서, 원본: https://www.abeautifulsite.net/parsing-urls-in-javascript
const parseURL = function(url) {
  var parser = document.createElement('a'),
    searchObject = {},
    queries, split, i;
  // Let the browser do the work
  parser.href = url;
  // Convert query string to object
  queries = parser.search.replace(/^\?/, '').split('&');
  for( i = 0; i < queries.length; i++ ) {
    split = queries[i].split('=');
    searchObject[split[0]] = split[1];
  }
  return {
    protocol: parser.protocol,
    host: parser.host,
    hostname: parser.hostname,
    port: parser.port,
    pathname: parser.pathname,
    search: parser.search,
    searchObject: searchObject, // 쿼리 스트링
    hash: parser.hash
  };
}

// 축약 링크로부터 코드를 추출한다.
const getShortCode = function(shortURL) {
  //URL의 형식은 반드시 '(프로토콜:)도메인/축약코드'로 되어 있어야 한다.
  const parsedURL = parseURL(shortURL)
  const pathname = parsedURL.pathname

  // 단일 경로가 아니면 종료
  if (pathname.match(/\//g).length > 1) {
    return {
      flag: false,
      msg: 'Invalid URL: Nested Pathname.'
    }
  }

  return {
    flag: true,
    shortCode: pathname.replace('/', '')
  }
}

export {getShortCode}