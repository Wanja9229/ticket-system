'use client';

import { useState } from 'react';

export default function Arrays() {
  const [output, setOutput] = useState('');

  const runExample = () => {
    let result = '';

    // 1. 배열 생성과 기본 조작
    result += `1. 배열 생성과 기본 조작:\n`;
    let tickets = ['A1', 'A2', 'A3', 'B1', 'B2'];
    result += `   초기 배열: [${tickets.join(', ')}]\n`;
    result += `   첫 번째 요소: ${tickets[0]}\n`;
    result += `   마지막 요소: ${tickets[tickets.length - 1]}\n`;
    result += `   배열 길이: ${tickets.length}\n\n`;

    // 2. 배열 메서드 - 추가/제거
    result += `2. 배열 요소 추가/제거:\n`;
    let seatNumbers = ['A1', 'A2'];
    
    // push: 끝에 추가
    seatNumbers.push('A3');
    result += `   push('A3'): [${seatNumbers.join(', ')}]\n`;
    
    // unshift: 앞에 추가
    seatNumbers.unshift('VIP1');
    result += `   unshift('VIP1'): [${seatNumbers.join(', ')}]\n`;
    
    // pop: 끝에서 제거
    let removed = seatNumbers.pop();
    result += `   pop(): [${seatNumbers.join(', ')}] (제거된 요소: ${removed})\n`;
    
    // shift: 앞에서 제거
    let removed2 = seatNumbers.shift();
    result += `   shift(): [${seatNumbers.join(', ')}] (제거된 요소: ${removed2})\n\n`;

    // 3. 고차 함수들
    result += `3. 배열 고차 함수들:\n`;
    const ticketData = [
      { seat: 'A1', price: 150000, sold: true, customer: '김철수' },
      { seat: 'A2', price: 150000, sold: false, customer: null },
      { seat: 'B1', price: 120000, sold: true, customer: '이영희' },
      { seat: 'B2', price: 120000, sold: false, customer: null },
      { seat: 'C1', price: 80000, sold: true, customer: '박민수' }
    ];

    // filter: 조건에 맞는 요소들만 걸러내기
    const soldTickets = ticketData.filter(ticket => ticket.sold);
    result += `   filter (판매된 티켓): ${soldTickets.length}장\n`;
    
    const availableTickets = ticketData.filter(ticket => !ticket.sold);
    result += `   filter (판매 가능): ${availableTickets.length}장\n`;

    // map: 각 요소를 변환하기
    const seatList = ticketData.map(ticket => ticket.seat);
    result += `   map (좌석 목록): [${seatList.join(', ')}]\n`;
    
    const priceList = ticketData.map(ticket => 
      ticket.price.toLocaleString('ko-KR') + '원'
    );
    result += `   map (가격 목록): [${priceList.join(', ')}]\n`;

    // find: 조건에 맞는 첫 번째 요소 찾기
    const expensiveTicket = ticketData.find(ticket => ticket.price >= 150000);
    result += `   find (15만원 이상): ${expensiveTicket.seat} (${expensiveTicket.price.toLocaleString()}원)\n`;

    // reduce: 배열을 하나의 값으로 줄이기
    const totalRevenue = soldTickets.reduce((sum, ticket) => sum + ticket.price, 0);
    result += `   reduce (총 매출): ${totalRevenue.toLocaleString('ko-KR')}원\n\n`;

    // 4. 배열 검색과 확인
    result += `4. 배열 검색과 확인:\n`;
    const seats = ['A1', 'A2', 'B1', 'C1', 'C2'];
    
    // includes: 특정 요소가 있는지 확인
    result += `   includes('B1'): ${seats.includes('B1')}\n`;
    result += `   includes('D1'): ${seats.includes('D1')}\n`;
    
    // indexOf: 특정 요소의 인덱스 찾기
    result += `   indexOf('C1'): ${seats.indexOf('C1')}\n`;
    result += `   indexOf('D1'): ${seats.indexOf('D1')} (없으면 -1)\n`;
    
    // some: 조건을 만족하는 요소가 하나라도 있는지
    const hasVipSeat = seats.some(seat => seat.startsWith('A'));
    result += `   some (A로 시작하는 좌석 있나?): ${hasVipSeat}\n`;
    
    // every: 모든 요소가 조건을 만족하는지
    const allValid = seats.every(seat => seat.length === 2);
    result += `   every (모든 좌석이 2글자?): ${allValid}\n\n`;

    // 5. 배열 정렬
    result += `5. 배열 정렬:\n`;
    const prices = [150000, 80000, 120000, 150000, 200000];
    
    // 숫자 오름차순 정렬
    const sortedPrices = [...prices].sort((a, b) => a - b);
    result += `   가격 오름차순: [${sortedPrices.map(p => p.toLocaleString()).join(', ')}]\n`;
    
    // 숫자 내림차순 정렬
    const sortedDesc = [...prices].sort((a, b) => b - a);
    result += `   가격 내림차순: [${sortedDesc.map(p => p.toLocaleString()).join(', ')}]\n`;
    
    // 문자열 정렬
    const seatNumbers2 = ['B2', 'A1', 'C1', 'A2', 'B1'];
    const sortedSeats = [...seatNumbers2].sort();
    result += `   좌석 정렬: [${sortedSeats.join(', ')}]\n\n`;

    // 6. 배열 변환과 결합
    result += `6. 배열 변환과 결합:\n`;
    const vipSeats = ['A1', 'A2'];
    const regularSeats = ['B1', 'B2', 'C1'];
    
    // concat: 배열 합치기
    const allSeats = vipSeats.concat(regularSeats);
    result += `   concat으로 합치기: [${allSeats.join(', ')}]\n`;
    
    // spread 연산자로 합치기
    const allSeats2 = [...vipSeats, ...regularSeats];
    result += `   spread로 합치기: [${allSeats2.join(', ')}]\n`;
    
    // slice: 배열 일부분 추출
    const firstThree = allSeats.slice(0, 3);
    result += `   slice(0, 3): [${firstThree.join(', ')}]\n`;
    
    // join: 배열을 문자열로 변환
    const seatString = allSeats.join(' / ');
    result += `   join(' / '): ${seatString}\n`;

    setOutput(result);
  };

  return (
    <div className="example-container">
      <div className="example-info">
        <h3>🎯 학습 목표</h3>
        <ul>
          <li><strong>배열 기초</strong>: 생성, 접근, 길이 확인</li>
          <li><strong>요소 조작</strong>: 추가, 제거, 수정</li>
          <li><strong>고차 함수</strong>: map, filter, reduce, find</li>
          <li><strong>검색/확인</strong>: includes, indexOf, some, every</li>
          <li><strong>정렬</strong>: sort 메서드와 비교 함수</li>
          <li><strong>변환/결합</strong>: slice, concat, join, spread</li>
        </ul>
      </div>

      <div className="code-section">
        <h3>📝 코드 예제</h3>
        <pre className="code-block">{`// 1. 배열 생성
const seats = ['A1', 'A2', 'B1'];
const prices = [150000, 120000, 80000];

// 2. 요소 추가/제거
seats.push('B2');           // 끝에 추가
seats.unshift('VIP1');      // 앞에 추가
const last = seats.pop();   // 끝에서 제거
const first = seats.shift(); // 앞에서 제거

// 3. 고차 함수들
const tickets = [
  { seat: 'A1', price: 150000, sold: true },
  { seat: 'A2', price: 150000, sold: false }
];

// 판매된 티켓만 필터링
const sold = tickets.filter(t => t.sold);

// 좌석 번호만 추출
const seatNumbers = tickets.map(t => t.seat);

// 총 매출 계산
const total = tickets
  .filter(t => t.sold)
  .reduce((sum, t) => sum + t.price, 0);

// 특정 티켓 찾기
const found = tickets.find(t => t.seat === 'A1');

// 4. 검색과 확인
seats.includes('A1');        // true/false
seats.indexOf('B1');         // 인덱스 또는 -1
seats.some(s => s.startsWith('A')); // 하나라도?
seats.every(s => s.length === 2);   // 모두?

// 5. 정렬
prices.sort((a, b) => a - b);  // 오름차순
prices.sort((a, b) => b - a);  // 내림차순

// 6. 배열 변환
const all = [...vipSeats, ...regularSeats]; // 합치기
const part = seats.slice(0, 3);             // 일부분
const str = seats.join(', ');               // 문자열로`}</pre>
      </div>

      <div className="interactive-section">
        <button onClick={runExample} className="run-button">
          🚀 예제 실행하기
        </button>
        
        {output && (
          <div className="output-section">
            <h4>📤 실행 결과:</h4>
            <pre className="output">{output}</pre>
          </div>
        )}
      </div>

      <div className="tips-section">
        <h3>💡 실무 팁</h3>
        <div className="tip">
          <strong>원본 배열 보존하기!</strong>
          <p>❌ <code>prices.sort()</code> (원본 변경)<br/>
             ✅ <code>[...prices].sort()</code> (복사본 정렬)</p>
        </div>
        <div className="tip">
          <strong>메서드 체이닝 활용하기!</strong>
          <p>✅ <code>data.filter().map().sort()</code><br/>
             단계별로 데이터를 변형하면 읽기 쉬움</p>
        </div>
        <div className="tip">
          <strong>적절한 메서드 선택하기!</strong>
          <p>• 찾기: <code>find()</code> vs <code>filter()</code><br/>
             • 확인: <code>some()</code> vs <code>every()</code><br/>
             • 변환: <code>map()</code> vs <code>forEach()</code></p>
        </div>
      </div>

      <style>{`
        .example-container {
          border: 1px solid #e1e5e9;
          border-radius: 8px;
          padding: 20px;
          margin: 20px 0;
        }

        .example-info ul {
          background: #f8f9fa;
          padding: 15px;
          border-radius: 6px;
          margin: 10px 0;
          columns: 2;
          column-gap: 30px;
        }

        .example-info li {
          margin: 8px 0;
          break-inside: avoid;
        }

        .code-section {
          margin: 20px 0;
        }

        .code-block {
          background: #2d3748;
          color: #e2e8f0;
          padding: 20px;
          border-radius: 6px;
          overflow-x: auto;
          font-family: 'Fira Code', monospace;
          line-height: 1.5;
          font-size: 14px;
        }

        .interactive-section {
          margin: 20px 0;
          text-align: center;
        }

        .run-button {
          background: #805ad5;
          color: white;
          border: none;
          padding: 12px 24px;
          border-radius: 6px;
          font-size: 16px;
          cursor: pointer;
          transition: background 0.2s;
        }

        .run-button:hover {
          background: #6b46c1;
        }

        .output-section {
          margin-top: 20px;
          text-align: left;
        }

        .output {
          background: #1a202c;
          color: #68d391;
          padding: 15px;
          border-radius: 6px;
          border-left: 4px solid #805ad5;
          font-family: monospace;
          white-space: pre-wrap;
          max-height: 400px;
          overflow-y: auto;
        }

        .tips-section {
          margin-top: 30px;
          background: #fffaf0;
          padding: 20px;
          border-radius: 6px;
          border-left: 4px solid #ed8936;
        }

        .tip {
          margin: 15px 0;
          padding: 10px;
          background: white;
          border-radius: 4px;
        }

        .tip strong {
          color: #c05621;
        }

        code {
          background: #edf2f7;
          padding: 2px 6px;
          border-radius: 3px;
          font-family: monospace;
          color: #2d3748;
        }

        @media (max-width: 768px) {
          .example-info ul {
            columns: 1;
          }
        }
      `}</style>
    </div>
  );
}
