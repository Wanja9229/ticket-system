'use client';

import { useState } from 'react';

export default function Functions() {
  const [output, setOutput] = useState('');

  const runExample = () => {
    let result = '';

    // 1. 함수 선언문
    function calculateTicketPrice(basePrice, isVip, discount = 0) {
      if (isVip) {
        basePrice = basePrice * 1.5; // VIP는 1.5배
      }
      return basePrice * (1 - discount);
    }

    // 2. 함수 표현식
    const formatPrice = function(price) {
      return price.toLocaleString('ko-KR') + '원';
    };

    // 3. 화살표 함수
    const getSeatGrade = (seatNumber) => {
      if (seatNumber.startsWith('A')) return 'VIP';
      if (seatNumber.startsWith('B')) return 'Premium';
      return 'Standard';
    };

    // 4. 즉시 실행 함수 (IIFE)
    const ticketSystem = (function() {
      let totalSales = 0; // 비공개 변수
      
      return {
        addSale: function(amount) {
          totalSales += amount;
        },
        getTotalSales: function() {
          return totalSales;
        },
        resetSales: function() {
          totalSales = 0;
        }
      };
    })();

    result += `1. 함수 선언문 예제:\n`;
    const price1 = calculateTicketPrice(100000, false, 0.1);
    const price2 = calculateTicketPrice(100000, true, 0.05);
    result += `   일반석(10% 할인): ${formatPrice(price1)}\n`;
    result += `   VIP석(5% 할인): ${formatPrice(price2)}\n\n`;

    result += `2. 화살표 함수 예제:\n`;
    const seats = ['A1', 'B3', 'C5'];
    seats.forEach(seat => {
      result += `   ${seat}석: ${getSeatGrade(seat)} 등급\n`;
    });
    result += `\n`;

    result += `3. 고차 함수 예제 (배열 메서드):\n`;
    const tickets = [
      { seat: 'A1', price: 150000, sold: true },
      { seat: 'A2', price: 150000, sold: false },
      { seat: 'B1', price: 120000, sold: true },
      { seat: 'C1', price: 80000, sold: false }
    ];

    // filter: 조건에 맞는 요소만 걸러내기
    const soldTickets = tickets.filter(ticket => ticket.sold);
    result += `   판매완료 티켓: ${soldTickets.length}장\n`;

    // map: 각 요소를 변환하기
    const seatNumbers = tickets.map(ticket => ticket.seat);
    result += `   모든 좌석: ${seatNumbers.join(', ')}\n`;

    // reduce: 배열을 하나의 값으로 줄이기
    const totalRevenue = soldTickets.reduce((sum, ticket) => sum + ticket.price, 0);
    result += `   총 매출: ${formatPrice(totalRevenue)}\n\n`;

    result += `4. 클로저와 모듈 패턴:\n`;
    ticketSystem.addSale(150000);
    ticketSystem.addSale(120000);
    result += `   매출 추가 후: ${formatPrice(ticketSystem.getTotalSales())}\n`;
    ticketSystem.resetSales();
    result += `   리셋 후: ${formatPrice(ticketSystem.getTotalSales())}\n\n`;

    result += `5. 콜백 함수 예제:\n`;
    function processPayment(amount, successCallback, errorCallback) {
      // 가상의 결제 처리
      const isSuccess = Math.random() > 0.3; // 70% 성공률
      
      setTimeout(() => {
        if (isSuccess) {
          successCallback(amount);
        } else {
          errorCallback('결제가 실패했습니다.');
        }
      }, 1000);
    }

    result += `   결제 처리 중... (실제로는 비동기 처리)\n`;

    setOutput(result);
  };

  return (
    <div className="example-container">
      <div className="example-info">
        <h3>🎯 학습 목표</h3>
        <ul>
          <li><strong>함수 선언</strong>: function 키워드로 함수 만들기</li>
          <li><strong>함수 표현식</strong>: 변수에 함수 할당하기</li>
          <li><strong>화살표 함수</strong>: ES6 간단한 함수 문법</li>
          <li><strong>고차 함수</strong>: 함수를 인자로 받는 함수</li>
          <li><strong>클로저</strong>: 함수의 스코프와 메모리</li>
          <li><strong>콜백</strong>: 비동기 처리의 기초</li>
        </ul>
      </div>

      <div className="code-section">
        <h3>📝 코드 예제</h3>
        <pre className="code-block">{`// 1. 함수 선언문 (Function Declaration)
function calculatePrice(basePrice, isVip, discount = 0) {
  if (isVip) basePrice *= 1.5;     // VIP는 1.5배
  return basePrice * (1 - discount); // 할인 적용
}

// 2. 함수 표현식 (Function Expression)
const formatPrice = function(price) {
  return price.toLocaleString('ko-KR') + '원';
};

// 3. 화살표 함수 (Arrow Function)
const getSeatGrade = (seat) => {
  if (seat.startsWith('A')) return 'VIP';
  if (seat.startsWith('B')) return 'Premium';
  return 'Standard';
};

// 4. 배열 메서드 (고차 함수)
const tickets = [
  { seat: 'A1', price: 150000, sold: true },
  { seat: 'B1', price: 120000, sold: false }
];

// filter: 조건에 맞는 것만
const soldTickets = tickets.filter(t => t.sold);

// map: 각 요소를 변환
const prices = tickets.map(t => t.price);

// reduce: 하나의 값으로 합치기
const total = tickets.reduce((sum, t) => sum + t.price, 0);

// 5. 콜백 함수
function processPayment(amount, onSuccess, onError) {
  // 비동기 처리
  if (paymentSuccess) {
    onSuccess(amount);
  } else {
    onError('결제 실패');
  }
}`}</pre>
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

      <div className="function-types">
        <h3>🔄 함수 선언 방법 비교</h3>
        <div className="comparison-grid">
          <div className="function-card">
            <h4>함수 선언문</h4>
            <pre>{`function greet(name) {
  return 'Hello ' + name;
}`}</pre>
            <div className="pros-cons">
              <div className="pros">
                <strong>장점:</strong>
                <ul>
                  <li>호이스팅으로 어디서든 호출 가능</li>
                  <li>읽기 쉽고 명확함</li>
                </ul>
              </div>
              <div className="cons">
                <strong>단점:</strong>
                <ul>
                  <li>함수 스코프만 지원</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="function-card">
            <h4>함수 표현식</h4>
            <pre>{`const greet = function(name) {
  return 'Hello ' + name;
};`}</pre>
            <div className="pros-cons">
              <div className="pros">
                <strong>장점:</strong>
                <ul>
                  <li>변수처럼 다룰 수 있음</li>
                  <li>조건부 함수 생성 가능</li>
                </ul>
              </div>
              <div className="cons">
                <strong>단점:</strong>
                <ul>
                  <li>호이스팅 안됨</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="function-card">
            <h4>화살표 함수</h4>
            <pre>{`const greet = (name) => {
  return 'Hello ' + name;
};

// 더 짧게
const greet = name => 'Hello ' + name;`}</pre>
            <div className="pros-cons">
              <div className="pros">
                <strong>장점:</strong>
                <ul>
                  <li>간결한 문법</li>
                  <li>this 바인딩 없음</li>
                </ul>
              </div>
              <div className="cons">
                <strong>단점:</strong>
                <ul>
                  <li>생성자로 사용 불가</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="real-examples">
        <h3>🎫 실제 티켓 시스템 함수들</h3>
        <div className="example-grid">
          <div className="example-card">
            <h4>🎯 가격 계산</h4>
            <pre>{`const calculateFinalPrice = (base, vip, discount) => {
  let price = vip ? base * 1.5 : base;
  return price * (1 - discount);
};`}</pre>
          </div>
          <div className="example-card">
            <h4>🔍 티켓 검색</h4>
            <pre>{`const findAvailableSeats = (tickets, section) => {
  return tickets
    .filter(t => !t.sold)
    .filter(t => t.seat.startsWith(section));
};`}</pre>
          </div>
          <div className="example-card">
            <h4>📊 매출 계산</h4>
            <pre>{`const getTotalRevenue = (sales) => {
  return sales.reduce((total, sale) => {
    return total + sale.amount;
  }, 0);
};`}</pre>
          </div>
          <div className="example-card">
            <h4>✅ 유효성 검증</h4>
            <pre>{`const validateTicket = (ticket) => {
  return ticket.seat && 
         ticket.price > 0 && 
         ticket.eventDate;
};`}</pre>
          </div>
        </div>
      </div>

      <div className="tips-section">
        <h3>💡 실무 팁</h3>
        <div className="tip">
          <strong>함수는 하나의 일만 하게 하세요!</strong>
          <p>❌ <code>calculatePriceAndSendEmail()</code><br/>
             ✅ <code>calculatePrice()</code>, <code>sendEmail()</code></p>
        </div>
        <div className="tip">
          <strong>함수명은 동사로 시작하세요!</strong>
          <p>✅ <code>getUserInfo()</code>, <code>calculateTotal()</code>, <code>validateForm()</code></p>
        </div>
        <div className="tip">
          <strong>화살표 함수는 간단한 연산에 사용하세요!</strong>
          <p>✅ <code>numbers.map(n =&gt; n * 2)</code><br/>
             ✅ <code>users.filter(u =&gt; u.age &gt;= 18)</code></p>
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
          background: #4299e1;
          color: white;
          border: none;
          padding: 12px 24px;
          border-radius: 6px;
          font-size: 16px;
          cursor: pointer;
          transition: background 0.2s;
        }

        .run-button:hover {
          background: #3182ce;
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
          border-left: 4px solid #4299e1;
          font-family: monospace;
          white-space: pre-wrap;
          max-height: 400px;
          overflow-y: auto;
        }

        .function-types {
          margin: 30px 0;
        }

        .comparison-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          gap: 20px;
          margin: 20px 0;
        }

        .function-card {
          border: 1px solid #e2e8f0;
          border-radius: 8px;
          padding: 15px;
          background: white;
        }

        .function-card h4 {
          margin-top: 0;
          color: #2d3748;
          border-bottom: 2px solid #4299e1;
          padding-bottom: 5px;
        }

        .function-card pre {
          background: #f7fafc;
          padding: 10px;
          border-radius: 4px;
          font-size: 12px;
          overflow-x: auto;
        }

        .pros-cons {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 15px;
          margin-top: 10px;
        }

        .pros, .cons {
          font-size: 12px;
        }

        .pros strong {
          color: #38a169;
        }

        .cons strong {
          color: #e53e3e;
        }

        .pros ul, .cons ul {
          margin: 5px 0;
          padding-left: 15px;
        }

        .real-examples {
          margin: 30px 0;
          background: #f8f9fa;
          padding: 20px;
          border-radius: 8px;
        }

        .example-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          gap: 15px;
          margin: 15px 0;
        }

        .example-card {
          background: white;
          border: 1px solid #e2e8f0;
          border-radius: 6px;
          padding: 15px;
        }

        .example-card h4 {
          margin-top: 0;
          color: #2d3748;
          font-size: 14px;
        }

        .example-card pre {
          background: #2d3748;
          color: #e2e8f0;
          padding: 10px;
          border-radius: 4px;
          font-size: 11px;
          overflow-x: auto;
          margin: 10px 0 0 0;
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
          
          .comparison-grid {
            grid-template-columns: 1fr;
          }
          
          .pros-cons {
            grid-template-columns: 1fr;
          }
          
          .example-grid {
            grid-template-columns: 1fr;
          }
        }
      `}</style>
    </div>
  );
}
