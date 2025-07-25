'use client';

import { useState } from 'react';

export default function TicketExample() {
  const [output, setOutput] = useState('');
  const [ticketSystem, setTicketSystem] = useState(null);

  // 티켓 시스템 초기화
  const initializeSystem = () => {
    const system = {
      events: [],
      customers: [],
      orders: [],
      
      // 이벤트 추가
      addEvent(eventData) {
        const event = {
          id: 'E' + (this.events.length + 1).toString().padStart(3, '0'),
          ...eventData,
          createdAt: new Date().toISOString(),
          tickets: []
        };
        this.events.push(event);
        return event;
      },
      
      // 티켓 생성 (좌석별)
      generateTickets(eventId, seatConfig) {
        const event = this.events.find(e => e.id === eventId);
        if (!event) return false;
        
        seatConfig.forEach(config => {
          for (let i = 1; i <= config.count; i++) {
            const ticket = {
              id: `${eventId}_${config.section}${i}`,
              eventId: eventId,
              seat: `${config.section}${i}`,
              section: config.section,
              price: config.price,
              status: 'available',
              customer: null,
              reservedAt: null,
              soldAt: null
            };
            event.tickets.push(ticket);
          }
        });
        return true;
      },
      
      // 고객 등록
      registerCustomer(customerData) {
        const customer = {
          id: 'C' + (this.customers.length + 1).toString().padStart(3, '0'),
          ...customerData,
          purchaseHistory: [],
          totalSpent: 0,
          registeredAt: new Date().toISOString()
        };
        this.customers.push(customer);
        return customer;
      },
      
      // 티켓 검색 (사용 가능한 것만)
      findAvailableTickets(eventId, section = null, maxPrice = null) {
        const event = this.events.find(e => e.id === eventId);
        if (!event) return [];
        
        return event.tickets.filter(ticket => {
          let match = ticket.status === 'available';
          if (section) match = match && ticket.section === section;
          if (maxPrice) match = match && ticket.price <= maxPrice;
          return match;
        });
      },
      
      // 유틸리티 메서드
      findTicketById(ticketId) {
        for (const event of this.events) {
          const ticket = event.tickets.find(t => t.id === ticketId);
          if (ticket) return ticket;
        }
        return null;
      },
      
      getEventStats(eventId) {
        const event = this.events.find(e => e.id === eventId);
        if (!event) return null;
        
        const total = event.tickets.length;
        const available = event.tickets.filter(t => t.status === 'available').length;
        const sold = event.tickets.filter(t => t.status === 'sold').length;
        
        const revenue = event.tickets
          .filter(t => t.status === 'sold')
          .reduce((sum, t) => sum + t.price, 0);
        
        return {
          eventName: event.name,
          total,
          available,
          sold,
          revenue,
          salesRate: ((sold / total) * 100).toFixed(1)
        };
      }
    };
    
    return system;
  };

  const runFullExample = () => {
    let result = '';
    
    // 시스템 초기화
    const system = initializeSystem();
    result += `🎫 티켓 예약 시스템 종합 예제\n`;
    result += `=====================================\n\n`;
    
    // 1. 이벤트 생성
    result += `1️⃣ 이벤트 생성:\n`;
    const concert = system.addEvent({
      name: 'IU 2024 콘서트',
      date: '2024-09-15',
      venue: '잠실실내체육관',
      artist: 'IU'
    });
    result += `   ✅ ${concert.name} (${concert.id}) 생성 완료\n`;
    result += `   📅 날짜: ${concert.date}\n`;
    result += `   📍 장소: ${concert.venue}\n\n`;
    
    // 2. 티켓 생성
    result += `2️⃣ 티켓 생성:\n`;
    const seatConfig = [
      { section: 'VIP', count: 3, price: 200000 },
      { section: 'A', count: 5, price: 150000 },
      { section: 'B', count: 10, price: 100000 }
    ];
    
    system.generateTickets(concert.id, seatConfig);
    result += `   🎟️ VIP석 3장 (${(200000).toLocaleString()}원)\n`;
    result += `   🎟️ A석 5장 (${(150000).toLocaleString()}원)\n`;
    result += `   🎟️ B석 10장 (${(100000).toLocaleString()}원)\n`;
    result += `   📊 총 ${concert.tickets.length}장 생성 완료\n\n`;
    
    // 3. 고객 등록
    result += `3️⃣ 고객 등록:\n`;
    const customers = [
      { name: '김철수', email: 'kim@email.com', phone: '010-1234-5678' },
      { name: '이영희', email: 'lee@email.com', phone: '010-2345-6789' },
      { name: '박민수', email: 'park@email.com', phone: '010-3456-7890' }
    ];
    
    customers.forEach(customerData => {
      const customer = system.registerCustomer(customerData);
      result += `   👤 ${customer.name} (${customer.id}) 등록\n`;
    });
    result += `\n`;
    
    // 4. 티켓 검색
    result += `4️⃣ 티켓 검색:\n`;
    const vipTickets = system.findAvailableTickets(concert.id, 'VIP');
    result += `   🔍 VIP석 검색: ${vipTickets.length}장 발견\n`;
    
    const affordableTickets = system.findAvailableTickets(concert.id, 'A', 150000);
    result += `   🔍 A석 15만원 이하: ${affordableTickets.length}장 발견\n\n`;
    
    // 5. 통계
    result += `5️⃣ 통계 분석:\n`;
    const stats = system.getEventStats(concert.id);
    result += `   📊 ${stats.eventName} 현황:\n`;
    result += `      • 총 티켓: ${stats.total}장\n`;
    result += `      • 판매완료: ${stats.sold}장\n`;
    result += `      • 판매가능: ${stats.available}장\n`;
    result += `      • 판매율: ${stats.salesRate}%\n`;
    result += `      • 총 매출: ${stats.revenue.toLocaleString()}원\n\n`;
    
    result += `🎉 시뮬레이션 완료!\n`;
    result += `=====================================\n`;
    result += `Week 1에서 배운 JavaScript 기초 문법을 모두 활용했습니다!\n\n`;
    result += `📚 사용된 개념들:\n`;
    result += `   • 변수와 상수 (let, const)\n`;
    result += `   • 데이터 타입 (string, number, boolean, array, object)\n`;
    result += `   • 함수 (선언문, 표현식, 화살표 함수)\n`;
    result += `   • 배열 메서드 (filter, map, reduce, find)\n`;
    result += `   • 객체 메서드와 this\n`;
    result += `   • 조건문과 반복문\n`;
    
    setOutput(result);
    setTicketSystem(system);
  };

  return (
    <div className="example-container">
      <div className="example-info">
        <h3>🎯 종합 예제 목표</h3>
        <p>Week 1에서 배운 모든 JavaScript 기초 문법을 활용한 <strong>실제 티켓 예약 시스템</strong>을 구현해봅시다!</p>
        <ul>
          <li><strong>객체 설계</strong>: 이벤트, 티켓, 고객, 주문 객체</li>
          <li><strong>배열 활용</strong>: filter, map, reduce로 데이터 처리</li>
          <li><strong>함수 설계</strong>: 예약, 결제, 검색 기능</li>
          <li><strong>통계 분석</strong>: 매출, 판매율, 고객 분석</li>
        </ul>
      </div>

      <div className="code-section">
        <h3>📝 핵심 코드 구조</h3>
        <pre className="code-block">{`// 티켓 시스템 객체 설계
const ticketSystem = {
  events: [],     // 이벤트 목록
  customers: [],  // 고객 목록  
  orders: [],     // 주문 목록
  
  // 이벤트 추가
  addEvent(eventData) {
    const event = {
      id: 'E' + (this.events.length + 1).toString().padStart(3, '0'),
      ...eventData,
      tickets: []
    };
    this.events.push(event);
    return event;
  },
  
  // 티켓 검색 (필터링)
  findAvailableTickets(eventId, section, maxPrice) {
    const event = this.events.find(e => e.id === eventId);
    return event.tickets.filter(ticket => {
      let match = ticket.status === 'available';
      if (section) match = match && ticket.section === section;
      if (maxPrice) match = match && ticket.price <= maxPrice;
      return match;
    });
  },
  
  // 통계 계산 (reduce 활용)
  getEventStats(eventId) {
    const event = this.events.find(e => e.id === eventId);
    const sold = event.tickets.filter(t => t.status === 'sold').length;
    const revenue = event.tickets
      .filter(t => t.status === 'sold')
      .reduce((sum, t) => sum + t.price, 0);
    
    return { sold, revenue, salesRate: (sold/total)*100 };
  }
};`}</pre>
      </div>

      <div className="interactive-section">
        <div className="button-group">
          <button onClick={runFullExample} className="run-button primary">
            🚀 종합 예제 실행하기
          </button>
        </div>
        
        {output && (
          <div className="output-section">
            <h4>📤 실행 결과:</h4>
            <pre className="output">{output}</pre>
          </div>
        )}
      </div>

      <div className="tips-section">
        <h3>💡 실무 개발 팁</h3>
        <div className="tip">
          <strong>객체 설계는 현실 세계를 모방하세요!</strong>
          <p>티켓, 고객, 이벤트 같은 실제 개념을 코드 객체로 표현하면 이해하기 쉽습니다.</p>
        </div>
        <div className="tip">
          <strong>배열 메서드를 체이닝으로 연결하세요!</strong>
          <p><code>tickets.filter().map().reduce()</code> 같은 방식으로 복잡한 데이터 처리를 간단하게!</p>
        </div>
        <div className="tip">
          <strong>함수명과 변수명을 명확하게!</strong>
          <p><code>findAvailableTickets()</code>, <code>calculateTotalRevenue()</code> 처럼 의도가 명확한 이름 사용</p>
        </div>
      </div>

      <style>{`
        .example-container {
          border: 1px solid #e1e5e9;
          border-radius: 8px;
          padding: 20px;
          margin: 20px 0;
        }

        .example-info {
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
          padding: 20px;
          border-radius: 8px;
          margin-bottom: 20px;
        }

        .example-info h3 {
          margin-top: 0;
          font-size: 1.5rem;
        }

        .example-info ul {
          background: rgba(255, 255, 255, 0.1);
          padding: 15px;
          border-radius: 6px;
          margin: 15px 0 0 0;
        }

        .example-info li {
          margin: 8px 0;
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
          font-size: 13px;
        }

        .interactive-section {
          margin: 20px 0;
          text-align: center;
        }

        .button-group {
          display: flex;
          gap: 15px;
          justify-content: center;
          margin-bottom: 20px;
        }

        .run-button {
          border: none;
          padding: 12px 24px;
          border-radius: 6px;
          font-size: 16px;
          cursor: pointer;
          transition: all 0.2s;
          font-weight: bold;
        }

        .run-button.primary {
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
        }

        .run-button.primary:hover {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .output-section {
          margin-top: 20px;
          text-align: left;
        }

        .output {
          background: #1a202c;
          color: #68d391;
          padding: 20px;
          border-radius: 6px;
          border-left: 4px solid #667eea;
          font-family: monospace;
          white-space: pre-wrap;
          max-height: 500px;
          overflow-y: auto;
          line-height: 1.4;
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
          padding: 15px;
          background: white;
          border-radius: 4px;
          border-left: 3px solid #667eea;
        }

        .tip strong {
          color: #667eea;
          display: block;
          margin-bottom: 8px;
        }

        code {
          background: #edf2f7;
          padding: 2px 6px;
          border-radius: 3px;
          font-family: monospace;
          color: #2d3748;
        }

        @media (max-width: 768px) {
          .button-group {
            flex-direction: column;
            align-items: center;
          }
        }
      `}</style>
    </div>
  );
}
