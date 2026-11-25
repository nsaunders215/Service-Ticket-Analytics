"""AI-assisted starter: synthetic service ticket metrics."""
from collections import Counter

def summarize(tickets):
    if any(t['hours'] < 0 for t in tickets):
        raise ValueError('Hours cannot be negative')
    count=len(tickets)
    return {'count':count,'average_hours':sum(t['hours'] for t in tickets)/count if count else None,'sla_breaches':sum(t['hours']>24 for t in tickets),'categories':dict(Counter(t['category'] for t in tickets))}

if __name__ == '__main__':
    print(summarize([{'hours':8,'category':'access'},{'hours':30,'category':'billing'}]))
